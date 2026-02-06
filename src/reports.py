def total_expenses(expenses):
    total = sum(e.amount for e in expenses)
    print(f"\nTotal Spending: ₹{total}")
