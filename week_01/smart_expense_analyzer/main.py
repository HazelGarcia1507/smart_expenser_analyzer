print("Smart Expense Analyzer")
   

expenses = [
        {"category": "food", "amount": 250},
        {"category": "transport", "amount": 100},
        {"category": "games", "amount": 500},
    ]

continue_choice = 'yes'
while continue_choice == "yes": 

    new_category = input("Enter expense category: ")
    new_amount = float(input("Enter expense amount: "))


    expenses.append(
            {"category": new_category, "amount": new_amount}
        )

    total = 0

    for expense in expenses:
        print(expense)

        total = total + expense["amount"]

    print("Total expenses:", total) 


    continue_choice = input("Add another expense? yes/no: ").lower()


# Future improvement:
# Validate yes/no input