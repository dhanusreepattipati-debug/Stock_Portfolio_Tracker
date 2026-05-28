# ==========================================
# Stock Portfolio Tracker
# ==========================================
# Description:
# A simple Python program to track stock investments.
# Users can enter stock symbols and quantities,
# and the program calculates the total investment value.
#
# Features:
# - Uses a predefined stock price dictionary
# - Accepts multiple stock entries
# - Calculates individual and total investment values
# - Saves portfolio summary to a text file
#
# Author: Your Name
# ==========================================

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 145,
    "MSFT": 330
}

print("\n========== STOCK PORTFOLIO TRACKER ==========\n")

portfolio = {}
total_investment = 0

# Number of different stocks user wants to add
try:
    stock_count = int(input("How many stocks do you want to add? : "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Taking stock details from user
for i in range(stock_count):
    print(f"\nStock Entry {i + 1}")

    stock_name = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()

    # Check if stock exists
    if stock_name not in stock_prices:
        print("Stock not available in tracker.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity entered.")
        continue

    # Calculate investment
    investment_value = stock_prices[stock_name] * quantity

    # Store in portfolio dictionary
    portfolio[stock_name] = {
        "quantity": quantity,
        "price": stock_prices[stock_name],
        "investment": investment_value
    }

    total_investment += investment_value

# Display Portfolio Summary
print("\n========== PORTFOLIO SUMMARY ==========\n")

if not portfolio:
    print("No valid stocks added.")
else:
    for stock, details in portfolio.items():
        print(f"Stock       : {stock}")
        print(f"Price       : ${details['price']}")
        print(f"Quantity    : {details['quantity']}")
        print(f"Investment  : ${details['investment']}")
        print("-" * 40)

    print(f"\nTotal Investment Value : ${total_investment}")

    # Save report to text file
    save_option = input("\nDo you want to save the report? (yes/no): ").lower()

    if save_option == "yes":
        with open("portfolio_report.txt", "w") as file:
            file.write("====== STOCK PORTFOLIO REPORT ======\n\n")

            for stock, details in portfolio.items():
                file.write(f"Stock       : {stock}\n")
                file.write(f"Price       : ${details['price']}\n")
                file.write(f"Quantity    : {details['quantity']}\n")
                file.write(f"Investment  : ${details['investment']}\n")
                file.write("-" * 40 + "\n")

            file.write(f"\nTotal Investment Value : ${total_investment}")

        print("\nReport saved successfully as 'portfolio_report.txt'")

print("\nThank you for using Stock Portfolio Tracker!")