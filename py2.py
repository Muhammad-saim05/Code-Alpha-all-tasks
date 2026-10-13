stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            investment = stock_prices[stock] * quantity
            total_investment += investment

            print("Stock price:", stock_prices[stock])
            print("Investment value:", investment)
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Stock not found.")

print("\nTotal Investment Value:", total_investment)

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Total Investment Value: " + str(total_investment))

    print("Result saved to portfolio.txt")

print("Thank you for using Stock Portfolio Tracker!")