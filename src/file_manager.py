import csv
from .expense import Expense


FILENAME = "expenses.csv"

def save_expense(expense):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    expenses.append(Expense(row[2], row[1], row[0], row[3]))
    except FileNotFoundError:
        pass
    return expenses
