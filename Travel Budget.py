
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter your total budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))

# Supplied exchange rates (1 unit of currency to INR)
rates = {
    "INR": 1.0,
    "USD": 83.0,
    "EUR": 90.0,
    "GBP": 105.0
}

expenses = {
    "Flight": (500, "USD"),
    "Hotel": (300, "EUR"),
    "Food": (100, "GBP"),
    "Shopping": (5000, "INR"),
    "Transport": (50, "USD")
}

total = 0
category_totals = {}

print("\n--- Travel Expense Report ---")

for category, details in expenses.items():
    amount, currency = details

    if currency in rates:
        converted = amount * rates[currency]
        fee = converted * fee_rate / 100
        final_amount = converted + fee

        category_totals[category] = final_amount
        total += final_amount

        print(f"{category}: {currency} {amount}")
        print(f"  Converted: INR {converted:.2f}")
        print(f"  Fee: INR {fee:.2f}")
        print(f"  Total: INR {final_amount:.2f}")

print("\n--- Budget Summary ---")
print(f"Budget: INR {budget:.2f}")
print(f"Total Expenses: INR {total:.2f}")
print(f"Remaining: INR {budget - total:.2f}")

if total > budget:
    print("Status: Budget Exceeded!")
else:
    print("Status: Within Budget")

largest = max(category_totals, key=category_totals.get)
print(f"Largest Expense: {largest}")
print(f"Amount: INR {category_totals[largest]:.2f}")
