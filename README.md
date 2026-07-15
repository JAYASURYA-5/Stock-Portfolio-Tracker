# Stock Portfolio Tracker

A professional-grade **Stock Portfolio Tracker** application featuring both a **Console CLI interface** and a **Web Dashboard interface** built with Python Flask and modern client-side features.

This application allows users to manage stock holdings (shares owned) and calculates real-time values, total overall investment valuation, and relative allocation percentages based on a predefined dictionary of stock tickers and prices.

---

## 📈 Predefined Market Stocks
The system tracks the following symbols and prices by default:
- **AAPL** (Apple): $178.50
- **MSFT** (Microsoft): $415.60
- **GOOGL** (Google): $152.30
- **AMZN** (Amazon): $185.75
- **TSLA** (Tesla): $174.60
- **NVDA** (NVIDIA): $875.12
- **META** (Meta): $505.40
- **NFLX** (Netflix): $622.30
- **AMD** (AMD): $168.90
- **INTC** (Intel): $35.20

---

## 🚀 Getting Started

### 1. Installation & Environment Setup

Navigate to the `stock` directory and install the necessary dependencies:

```bash
cd stock
pip install -r requirements.txt
```

---

### 2. Run the Console Portfolio Tracker (CLI)
For a terminal-based experience, execute:

```bash
python console_tracker.py
```

**Features in CLI:**
* **View Prices**: Displays all available stock ticker prices.
* **Manage Assets**: Prompt-based interactive commands to add, update, and remove stock quantities.
* **Arithmetics**: Instantly calculates individual value sizes and full portfolio net asset value.
* **Exporting**: Save current configurations to a local `.txt` or `.csv` spreadsheet file (e.g. `portfolio_export_20260715_120000.csv`).

---

### 3. Run the Web Portfolio Dashboard (Flask App)
For a modern, responsive web application, run:

```bash
python app.py
```

After launching the server locally, open your web browser and navigate to:
```text
http://127.0.0.1:5000
```

**Features in Web App:**
* **Fluid Glassmorphism UI**: Beautiful dark-themed aesthetic with vibrant gradients, glowing focus highlights, and sliding toast banners.
* **Dynamic Charting**: Automatically calculates and charts asset allocations in a smooth Chart.js doughnut graph.
* **Live Price References**: Quick references for ticker values. Clicking a symbol in the reference list auto-populates the select dropdown.
* **Browser Exports**: One-click download of the portfolio structure in clean formatting as `.csv` or `.txt`.
* **Session Storage**: Automatically keeps track of your current session's portfolio when navigating or reloading.

---

## 🛠️ File Structure
* [console_tracker.py](file:///d:/coding/INTERNSHIP/code%20alfa/stock/console_tracker.py) - Contains core price listings, calculations, and the CLI loops.
* [app.py](file:///d:/coding/INTERNSHIP/code%20alfa/stock/app.py) - Serves as the Flask web server, wrapping API routes.
* [templates/index.html](file:///d:/coding/INTERNSHIP/code%20alfa/stock/templates/index.html) - Structural markup featuring dashboard containers and CDNs.
* [static/css/style.css](file:///d:/coding/INTERNSHIP/code%20alfa/stock/static/css/style.css) - Premium CSS design rules (dark styles, glass filters).
* [static/js/app.js](file:///d:/coding/INTERNSHIP/code%20alfa/stock/static/js/app.js) - Asynchronous fetch operations, toast messaging, and Chart.js bindings.
* [requirements.txt](file:///d:/coding/INTERNSHIP/code%20alfa/stock/requirements.txt) - List of application library dependencies.
