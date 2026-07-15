from flask import Flask, render_template, request, jsonify, session, Response
from console_tracker import STOCK_PRICES, calculate_portfolio_details
import io
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "stock-tracker-secure-secret-key-alfa"

# Helper to load portfolio from session or initialize it
def get_session_portfolio():
    if "portfolio" not in session:
        session["portfolio"] = {}
    return session["portfolio"]

def save_session_portfolio(portfolio):
    session["portfolio"] = portfolio
    session.modified = True

@app.route("/")
def home():
    """Renders the main dashboard interface."""
    return render_template("index.html")

@app.route("/api/prices", methods=["GET"])
def get_prices():
    """API endpoint to get the list of supported stocks and prices."""
    return jsonify({
        "success": True,
        "prices": STOCK_PRICES
    })

@app.route("/api/portfolio", methods=["GET"])
def get_portfolio():
    """API endpoint to get the current portfolio values and breakdown."""
    portfolio = get_session_portfolio()
    holdings, total_value = calculate_portfolio_details(portfolio)
    
    # Add allocation percentage to each holding
    for hold in holdings:
        if total_value > 0:
            hold["allocation"] = round((hold["value"] / total_value) * 100, 2)
        else:
            hold["allocation"] = 0.0

    return jsonify({
        "success": True,
        "holdings": holdings,
        "total_value": round(total_value, 2),
        "available_stocks": STOCK_PRICES
    })

@app.route("/api/portfolio/add", methods=["POST"])
def add_stock():
    """API endpoint to add or update stock holdings."""
    data = request.get_json() or {}
    symbol = data.get("symbol", "").strip().upper()
    shares_str = str(data.get("shares", "")).strip()

    if not symbol:
        return jsonify({"success": False, "error": "Stock symbol is required."}), 400
    
    if symbol not in STOCK_PRICES:
        return jsonify({
            "success": False, 
            "error": f"Stock symbol '{symbol}' is not supported. Supported symbols: {', '.join(sorted(STOCK_PRICES.keys()))}"
        }), 400

    try:
        shares = float(shares_str)
        if shares <= 0:
            return jsonify({"success": False, "error": "Number of shares must be greater than 0."}), 400
    except ValueError:
        return jsonify({"success": False, "error": "Invalid shares value. Must be a numeric value."}), 400

    portfolio = get_session_portfolio()
    portfolio[symbol] = shares
    save_session_portfolio(portfolio)

    return jsonify({
        "success": True,
        "message": f"Successfully updated {symbol} with {shares:.4f} shares."
    })

@app.route("/api/portfolio/delete", methods=["POST"])
def delete_stock():
    """API endpoint to remove a stock from the portfolio."""
    data = request.get_json() or {}
    symbol = data.get("symbol", "").strip().upper()

    portfolio = get_session_portfolio()
    if symbol in portfolio:
        del portfolio[symbol]
        save_session_portfolio(portfolio)
        return jsonify({
            "success": True,
            "message": f"Removed {symbol} from portfolio."
        })
    
    return jsonify({
        "success": False,
        "error": f"Stock {symbol} not found in portfolio."
    }), 404

@app.route("/api/portfolio/clear", methods=["POST"])
def clear_portfolio():
    """API endpoint to empty the portfolio."""
    save_session_portfolio({})
    return jsonify({
        "success": True,
        "message": "Portfolio cleared."
    })

@app.route("/api/portfolio/export", methods=["GET"])
def export_portfolio():
    """API endpoint that generates and serves portfolio exports."""
    format_type = request.args.get("format", "csv").strip().lower()
    portfolio = get_session_portfolio()

    if not portfolio:
        return "Cannot export an empty portfolio", 400

    holdings, total = calculate_portfolio_details(portfolio)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.{format_type}"

    if format_type == "csv":
        # Generate CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Stock Symbol", "Shares Owned", "Current Price ($)", "Total Value ($)", "Allocation (%)"])
        for hold in holdings:
            alloc = round((hold["value"] / total) * 100, 2) if total > 0 else 0
            writer.writerow([hold["symbol"], hold["shares"], f"{hold['price']:.2f}", f"{hold['value']:.2f}", f"{alloc:.2f}%"])
        writer.writerow([])
        writer.writerow(["TOTAL VALUE", "", "", f"{total:.2f}", "100.00%"])
        
        mem_file = io.BytesIO(output.getvalue().encode("utf-8"))
        output.close()
        
        return Response(
            mem_file,
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    elif format_type == "txt":
        # Generate TXT layout in memory
        output = io.StringIO()
        output.write("=" * 70 + "\n")
        output.write("             STOCK PORTFOLIO TRACKER SUMMARY             \n")
        output.write(f"             Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        output.write("=" * 70 + "\n\n")
        output.write(f"{'Stock':<10} | {'Shares':<12} | {'Price (USD)':<14} | {'Total Value (USD)':<16} | {'Allocation':<10}\n")
        output.write("-" * 70 + "\n")
        for hold in holdings:
            alloc = f"{round((hold['value'] / total) * 100, 2):.2f}%" if total > 0 else "0.00%"
            output.write(f"{hold['symbol']:<10} | {hold['shares']:<12.4f} | ${hold['price']:<13.2f} | ${hold['value']:<15.2f} | {alloc:<10}\n")
        output.write("-" * 70 + "\n")
        output.write(f"{'TOTAL PORTFOLIO VALUE:':<43} | ${total:<15.2f} | 100.00%\n")
        output.write("=" * 70 + "\n")

        mem_file = io.BytesIO(output.getvalue().encode("utf-8"))
        output.close()

        return Response(
            mem_file,
            mimetype="text/plain",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )

    return "Invalid export format. Use 'csv' or 'txt'", 400

if __name__ == "__main__":
    print("Starting Alfa Stock Portfolio Tracker Web Server...")
    app.run(host="127.0.0.1", port=5000, debug=True)
