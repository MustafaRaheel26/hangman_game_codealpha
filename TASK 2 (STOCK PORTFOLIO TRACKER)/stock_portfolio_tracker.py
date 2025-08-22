# Stock Portfolio Tracker

# Hardcoded stock prices (Dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140,
    "AMZN": 130
}

# Function to calculate total investment
def calculate_total():
    total_value = 0
    portfolio = {}

    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when finished.\n")

    while True:
        stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock_name == "DONE":
            break
        if stock_name not in stock_prices:
            print("❌ Stock not found in list. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        value = stock_prices[stock_name] * quantity
        total_value += value
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    return total_value, portfolio

# Main program
total, portfolio = calculate_total()

print("\n📊 Your Portfolio Summary 📊")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares @ ${stock_prices[stock]} each")
print(f"\n💰 Total Investment Value: ${total}")

# Optionally save to file
save_option = input("\nDo you want to save the result? (yes/no): ").lower()
if save_option == "yes":
    file_type = input("Save as (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ${total}")
        print("✅ Saved as portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as f:
            f.write("Stock,Quantity,Price per Share,Total Value\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{qty * stock_prices[stock]}\n")
            f.write(f"Total,,,{total}")
        print("✅ Saved as portfolio.csv")

    else:
        print("❌ Invalid file type. Not saved.")