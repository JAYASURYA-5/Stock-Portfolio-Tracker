import os
import csv
from datetime import datetime

# Predefined dictionary containing stock symbols and their current prices
STOCK_PRICES = {
    "AAPL": 178.50,
    "MSFT": 415.60,
    "GOOGL": 152.30,
    "AMZN": 185.75,
    "TSLA": 174.60,
    "NVDA": 875.12,
    "META": 505.40,
    "NFLX": 622.30,
    "AMD": 168.90,
    "INTC": 35.20
}

def display_header():
    """Prints a styled header for the CLI."""
    print("=" * 60)
    print("           ALFA STOCK PORTFOLIO TRACKER (CLI)           ")
    print("=" * 60)

def display_menu():
    """Displays the main menu choices."""
    print("\n[1] View Available Stocks & Live Prices")
    print("[2] Add / Update Stock in Portfolio")
    print("[3] Remove Stock from Portfolio")
    print("[4] View Current Portfolio Summary")
    print("[5] Export Portfolio to File (.txt or .csv)")
    print("[6] Exit Program")
    print("-" * 60)

def show_available_stocks():
    """Displays the hardcoded list of available stocks and prices."""
    print("\n--- Available Stocks and Prices ---")
    print(f"{'Stock Symbol':<15} | {'Current Price (USD)':<20}")
    print("-" * 40)
    for symbol, price in sorted(STOCK_PRICES.items()):
        print(f"{symbol:<15} | ${price:<20.2f}")
    print("-" * 40)

def calculate_portfolio_details(portfolio):
    """Calculates holdings details and overall valuation.
    
    Args:
        portfolio (dict): Dictionary mapping uppercase stock symbol to float shares.
    
    Returns:
        tuple: (list of dicts, float total_value)
    """
    holdings_list = []
    total_value = 0.0
    for symbol, shares in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = shares * price
        total_value += value
        holdings_list.append({
            "symbol": symbol,
            "shares": shares,
            "price": price,
            "value": value
        })
    return holdings_list, total_value

def display_portfolio(portfolio):
    """Displays the user's current holdings in a clean table."""
    if not portfolio:
        print("\n[!] Your portfolio is currently empty. Add stocks to start tracking!")
        return

    holdings_list, total_value = calculate_portfolio_details(portfolio)
    
    print("\n" + "=" * 65)
    print("                      YOUR CURRENT PORTFOLIO                    ")
    print("=" * 65)
    print(f"{'Stock':<10} | {'Shares':<12} | {'Price (USD)':<14} | {'Total Value (USD)':<18}")
    print("-" * 65)
    for hold in holdings_list:
        print(f"{hold['symbol']:<10} | {hold['shares']:<12.4f} | ${hold['price']:<13.2f} | ${hold['value']:<17.2f}")
    print("-" * 65)
    print(f"{'TOTAL PORTFOLIO VALUE:':<43} | ${total_value:<17.2f}")
    print("=" * 65)

def export_portfolio(portfolio):
    """Prompts the user to save their portfolio to TXT or CSV."""
    if not portfolio:
        print("\n[!] Cannot export an empty portfolio.")
        return

    print("\n--- Export Portfolio ---")
    format_choice = input("Enter export format (csv/txt): ").strip().lower()
    while format_choice not in ["csv", "txt"]:
        format_choice = input("Invalid choice. Please enter 'csv' or 'txt': ").strip().lower()

    filename = input("Enter output filename (press Enter for default): ").strip()
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_export_{timestamp}.{format_choice}"
    else:
        if not filename.endswith(f".{format_choice}"):
            filename += f".{format_choice}"

    holdings, total = calculate_portfolio_details(portfolio)

    try:
        if format_choice == "csv":
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock Symbol", "Shares Owned", "Current Price ($)", "Total Value ($)"])
                for hold in holdings:
                    writer.writerow([hold["symbol"], hold["shares"], f"{hold['price']:.2f}", f"{hold['value']:.2f}"])
                writer.writerow([])
                writer.writerow(["TOTAL VALUE", "", "", f"{total:.2f}"])
            print(f"\n[+] Portfolio successfully exported to CSV file: {os.path.abspath(filename)}")

        elif format_choice == "txt":
            with open(filename, mode="w", encoding="utf-8") as f:
                f.write("=" * 65 + "\n")
                f.write("             STOCK PORTFOLIO TRACKER SUMMARY             \n")
                f.write(f"             Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 65 + "\n\n")
                f.write(f"{'Stock':<10} | {'Shares':<12} | {'Price (USD)':<14} | {'Total Value (USD)':<18}\n")
                f.write("-" * 65 + "\n")
                for hold in holdings:
                    f.write(f"{hold['symbol']:<10} | {hold['shares']:<12.4f} | ${hold['price']:<13.2f} | ${hold['value']:<17.2f}\n")
                f.write("-" * 65 + "\n")
                f.write(f"{'TOTAL PORTFOLIO VALUE:':<43} | ${total:<17.2f}\n")
                f.write("=" * 65 + "\n")
            print(f"\n[+] Portfolio successfully exported to TXT file: {os.path.abspath(filename)}")

    except Exception as e:
        print(f"\n[X] Error exporting portfolio to file: {e}")

def main():
    portfolio = {} # Key: Stock Symbol (str), Value: Shares (float)
    
    while True:
        display_header()
        display_menu()
        
        choice = input("Enter your option (1-6): ").strip()
        
        if choice == "1":
            show_available_stocks()
            input("\nPress Enter to return to main menu...")
            
        elif choice == "2":
            show_available_stocks()
            symbol = input("Enter Stock Symbol to add/update: ").strip().upper()
            if symbol not in STOCK_PRICES:
                print(f"\n[X] Invalid stock symbol '{symbol}'. We currently only track stocks listed in our dictionary.")
                print(f"Supported stocks: {', '.join(sorted(STOCK_PRICES.keys()))}")
            else:
                try:
                    shares_input = input(f"Enter the number of shares owned for {symbol}: ").strip()
                    shares = float(shares_input)
                    if shares <= 0:
                        print("\n[X] Shares quantity must be greater than 0.")
                    else:
                        portfolio[symbol] = shares
                        print(f"\n[+] Successfully updated {symbol} holding with {shares:.4f} shares.")
                except ValueError:
                    print("\n[X] Invalid input. Shares must be a number.")
            input("\nPress Enter to return to main menu...")
            
        elif choice == "3":
            if not portfolio:
                print("\n[!] Your portfolio is empty. Nothing to remove.")
            else:
                display_portfolio(portfolio)
                symbol = input("Enter Stock Symbol to remove: ").strip().upper()
                if symbol in portfolio:
                    del portfolio[symbol]
                    print(f"\n[-] Successfully removed {symbol} from portfolio.")
                else:
                    print(f"\n[X] Stock symbol '{symbol}' is not currently in your portfolio.")
            input("\nPress Enter to return to main menu...")
            
        elif choice == "4":
            display_portfolio(portfolio)
            input("\nPress Enter to return to main menu...")
            
        elif choice == "5":
            export_portfolio(portfolio)
            input("\nPress Enter to return to main menu...")
            
        elif choice == "6":
            print("\nThank you for using Alfa Stock Portfolio Tracker. Goodbye!")
            break
            
        else:
            print("\n[X] Invalid option selected. Please choose a value from 1 to 6.")
            input("\nPress Enter to return to main menu...")
            
        # Clear screen helper (cross-platform, but optional)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

if __name__ == "__main__":
    main()
