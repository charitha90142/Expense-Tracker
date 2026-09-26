expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Total Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpense Details:")
            for expense in expenses:
                print("Name:", expense["name"])
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("----------------")

    elif choice == "3":
        name = input("Enter expense name to search: ")

        found = False

        for expense in expenses:
            if expense["name"].lower() == name.lower():
                print("Expense Found!")
                print("Name:", expense["name"])
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                found = True

        if not found:
            print("Expense not found.")

    elif choice == "4":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expense:", total)

    elif choice == "5":
        name = input("Enter expense name to delete: ")

        for expense in expenses:
            if expense["name"].lower() == name.lower():
                expenses.remove(expense)
                print("Expense deleted successfully!")
                break
        else:
            print("Expense not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")