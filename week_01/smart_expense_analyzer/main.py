print("Smart Expense Analyzer")

expenses = [
    {"category": "food", "amount": 250},
    {"category": "transport", "amount": 100},
    {"category": "games", "amount": 500}
]

total = 0

for expense in expenses:
    print(expense)

    total = total + expense["amount"]

print("Total expenses:", total)