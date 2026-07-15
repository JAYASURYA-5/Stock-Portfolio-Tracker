let allocationChart = null;

// Initialize the dashboard on load
document.addEventListener("DOMContentLoaded", () => {
    fetchPortfolio();
    setupEventListeners();
});

// Setup global event listeners
function setupEventListeners() {
    // Add event listeners or additional static layout bindings if needed
}

// Fetch entire dashboard state (prices + holdings)
async function fetchPortfolio() {
    try {
        const response = await fetch("/api/portfolio");
        const data = await response.json();
        
        if (data.success) {
            renderStockSelect(data.available_stocks);
            renderPriceTicker(data.available_stocks);
            renderReferenceFeed(data.available_stocks);
            renderHoldingsTable(data.holdings, data.total_value);
            renderStats(data.holdings, data.total_value);
            renderChart(data.holdings);
            updateExportLinks(data.holdings.length > 0);
        } else {
            showToast(data.error || "Failed to load portfolio.", "error");
        }
    } catch (err) {
        console.error("Error fetching portfolio:", err);
        showToast("Error connecting to web server.", "error");
    }
}

// Render dropdown list of stocks
function renderStockSelect(prices) {
    const select = document.getElementById("stock-select");
    const currentValue = select.value;
    
    // Clear keeping the disabled option
    select.innerHTML = '<option value="" disabled selected>-- Select a Symbol --</option>';
    
    Object.keys(prices).sort().forEach(sym => {
        const opt = document.createElement("option");
        opt.value = sym;
        opt.textContent = `${sym} ($${prices[sym].toFixed(2)})`;
        select.appendChild(opt);
    });

    if (currentValue && prices[currentValue]) {
        select.value = currentValue;
    }
}

// Render top scrolling live ticker
function renderPriceTicker(prices) {
    const track = document.getElementById("ticker-track");
    track.innerHTML = "";
    
    const symbols = Object.keys(prices).sort();
    
    // Double the items to make the ticker animation seamless
    const items = [...symbols, ...symbols];
    
    items.forEach((sym, index) => {
        const price = prices[sym];
        // Calculate a mocked variation/percentage change for aesthetics
        const mockChange = ((sym.charCodeAt(0) % 5) - 2) * 0.45;
        const changeSign = mockChange >= 0 ? "+" : "";
        const changeClass = mockChange >= 0 ? "success" : "danger";
        
        const item = document.createElement("div");
        item.className = "ticker-item";
        item.innerHTML = `
            <span class="symbol">${sym}</span>
            <span class="price">$${price.toFixed(2)}</span>
            <span class="change" style="color: var(--${changeClass});">
                ${changeSign}${mockChange.toFixed(2)}%
            </span>
        `;
        track.appendChild(item);
    });
}

// Render price list sidebar reference
function renderReferenceFeed(prices) {
    const container = document.getElementById("ref-stock-list");
    container.innerHTML = "";
    
    Object.keys(prices).sort().forEach(sym => {
        const item = document.createElement("div");
        item.className = "ref-stock-item";
        item.innerHTML = `
            <span class="sym">${sym}</span>
            <span class="prc">$${prices[sym].toFixed(2)}</span>
        `;
        
        // When clicking on a stock in reference list, prepopulate the dropdown selection
        item.addEventListener("click", () => {
            document.getElementById("stock-select").value = sym;
            document.getElementById("stock-shares").focus();
            showToast(`Selected ${sym} from market feed.`, "info");
        });
        
        container.appendChild(item);
    });
}

// Calculate and update top summary stat cards
function renderStats(holdings, totalValue) {
    document.getElementById("stat-total-value").textContent = `$${totalValue.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
    document.getElementById("stat-holdings-count").textContent = holdings.length;

    let dominantText = "N/A";
    let maxVal = -1;
    holdings.forEach(hold => {
        if (hold.value > maxVal) {
            maxVal = hold.value;
            dominantText = `${hold.symbol} (${hold.allocation}%)`;
        }
    });
    
    document.getElementById("stat-dominant-stock").textContent = dominantText;
}

// Render stock holdings table rows
function renderHoldingsTable(holdings, totalValue) {
    const tbody = document.getElementById("portfolio-table-body");
    tbody.innerHTML = "";
    
    if (holdings.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="6">
                    <div class="empty-table-state">
                        <svg viewBox="0 0 24 24">
                            <path d="M19.36 10.04L20.57 7.62c.15-.31-.07-.67-.41-.67H17V5c0-1.1-.9-2-2-2H9c-1.1 0-2 .9-2 2v2H3.44c-.34 0-.56.36-.41.67l1.21 2.42c.28.56.85.91 1.48.91H7v8c0 1.1.9 2 2 2h6c1.1 0 2-.9 2-2v-8h1.27c.64 0 1.21-.35 1.49-.91M9 5h6v2H9V5m6 15H9v-8h6v8z"/>
                        </svg>
                        <p>No active investments found</p>
                        <span>Add stocks using the panel on the left to start tracking.</span>
                    </div>
                </td>
            </tr>
        `;
        return;
    }
    
    holdings.forEach(hold => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>
                <div class="td-stock">
                    <span class="stock-tag">${hold.symbol}</span>
                </div>
            </td>
            <td class="td-numeric">${hold.shares.toFixed(4)}</td>
            <td class="td-numeric">$${hold.price.toFixed(2)}</td>
            <td class="td-numeric" style="font-weight: 700;">$${hold.value.toFixed(2)}</td>
            <td>
                <span class="allocation-badge">${hold.allocation}%</span>
            </td>
            <td style="text-align: right;">
                <button onclick="deleteHolding('${hold.symbol}')" class="btn-delete" title="Remove ${hold.symbol}">
                    <svg viewBox="0 0 24 24">
                        <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
                    </svg>
                </button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

// Render dynamic allocation doughnut chart
function renderChart(holdings) {
    const chartDiv = document.getElementById("chart-container-div");
    const fallbackDiv = document.getElementById("chart-fallback");
    
    if (holdings.length === 0) {
        chartDiv.style.display = "none";
        fallbackDiv.style.display = "flex";
        if (allocationChart) {
            allocationChart.destroy();
            allocationChart = null;
        }
        return;
    }
    
    chartDiv.style.display = "block";
    fallbackDiv.style.display = "none";
    
    const labels = holdings.map(h => h.symbol);
    const values = holdings.map(h => h.value);
    
    // Harmonious modern color chart palette
    const colors = [
        "#6366f1", // Indigo
        "#10b981", // Emerald
        "#0ea5e9", // Sky Blue
        "#eab308", // Yellow
        "#a855f7", // Purple
        "#f43f5e", // Rose
        "#f97316", // Orange
        "#84cc16", // Lime
        "#06b6d4", // Cyan
        "#ec4899"  // Pink
    ];
    
    const borderColors = colors.map(c => "#0b0f19");

    if (allocationChart) {
        // Update data values to trigger smooth transition animations
        allocationChart.data.labels = labels;
        allocationChart.data.datasets[0].data = values;
        allocationChart.data.datasets[0].backgroundColor = colors.slice(0, holdings.length);
        allocationChart.update();
    } else {
        const ctx = document.getElementById("allocation-chart").getContext("2d");
        allocationChart = new Chart(ctx, {
            type: "doughnut",
            data: {
                labels: labels,
                datasets: [{
                    data: values,
                    backgroundColor: colors.slice(0, holdings.length),
                    borderColor: borderColors.slice(0, holdings.length),
                    borderWidth: 2,
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false // We will hide standard legend for micro design spaces
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const val = context.parsed;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = ((val / total) * 100).toFixed(2);
                                return ` ${context.label}: $${val.toFixed(2)} (${percentage}%)`;
                            }
                        },
                        backgroundColor: "#161f30",
                        titleFont: { family: "Plus Jakarta Sans", weight: "bold" },
                        bodyFont: { family: "Inter" },
                        borderColor: "rgba(255,255,255,0.08)",
                        borderWidth: 1
                    }
                },
                cutout: "70%"
            }
        });
    }
}

// Show/Hide Export controls depending on active portfolio holdings
function updateExportLinks(hasHoldings) {
    const controls = document.getElementById("export-controls");
    if (hasHoldings) {
        controls.style.display = "flex";
        document.getElementById("export-csv-btn").href = "/api/portfolio/export?format=csv";
        document.getElementById("export-txt-btn").href = "/api/portfolio/export?format=txt";
    } else {
        controls.style.display = "none";
    }
}

// Handle Form Submission: Add / Update Stock
async function addOrUpdateHolding() {
    const symbol = document.getElementById("stock-select").value;
    const sharesVal = document.getElementById("stock-shares").value;
    
    if (!symbol) {
        showToast("Please choose a stock symbol.", "error");
        return;
    }
    
    const shares = parseFloat(sharesVal);
    if (isNaN(shares) || shares <= 0) {
        showToast("Shares owned must be a positive number.", "error");
        return;
    }
    
    try {
        const response = await fetch("/api/portfolio/add", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symbol, shares })
        });
        const data = await response.json();
        
        if (data.success) {
            showToast(data.message, "success");
            document.getElementById("stock-shares").value = "";
            fetchPortfolio();
        } else {
            showToast(data.error || "Failed to update holding.", "error");
        }
    } catch (err) {
        console.error(err);
        showToast("Error updating holding.", "error");
    }
}

// Delete specific stock item
async function deleteHolding(symbol) {
    try {
        const response = await fetch("/api/portfolio/delete", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symbol })
        });
        const data = await response.json();
        
        if (data.success) {
            showToast(data.message, "success");
            fetchPortfolio();
        } else {
            showToast(data.error || "Failed to delete holding.", "error");
        }
    } catch (err) {
        console.error(err);
        showToast("Error deleting stock.", "error");
    }
}

// Clear entire portfolio list
async function clearPortfolio() {
    if (!confirm("Are you sure you want to empty your portfolio? All holdings will be removed.")) {
        return;
    }
    
    try {
        const response = await fetch("/api/portfolio/clear", {
            method: "POST"
        });
        const data = await response.json();
        
        if (data.success) {
            showToast(data.message, "success");
            fetchPortfolio();
        } else {
            showToast("Failed to reset portfolio.", "error");
        }
    } catch (err) {
        console.error(err);
        showToast("Error resetting portfolio.", "error");
    }
}

// Custom Toast Notifier helper
function showToast(message, type = "info") {
    const container = document.getElementById("toast-container");
    
    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <div class="toast-content">${message}</div>
        <button class="toast-close" onclick="this.parentElement.remove();">&times;</button>
    `;
    
    container.appendChild(toast);
    
    // Auto-remove after 4.5 seconds
    setTimeout(() => {
        if (toast.parentElement) {
            toast.style.opacity = "0";
            toast.style.transform = "translateY(15px)";
            toast.style.transition = "all 0.3s ease";
            setTimeout(() => toast.remove(), 300);
        }
    }, 4500);
}
