from .expense import Expense
from .file_manager import save_expense, load_expenses
from .reports import total_expenses


def show_menu():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL FINANCE MANAGER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Amount: ")
            category = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            description = input("Description: ")

            try:
                expense = Expense(amount, category, date, description)
                save_expense(expense)
                expenses.append(expense)
                print("✅ Expense added!")
            except:
                print("❌ Invalid data!")

        elif choice == "2":
            for e in expenses:
                print(e)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            print("Goodbye!")
            break
