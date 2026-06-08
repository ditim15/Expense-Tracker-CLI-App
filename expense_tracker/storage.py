import json
from expense_tracker.expense import Expense

FILE = "expenses.json"

def read_expenses():
    try:
        with open(FILE, "r") as f:
            return [Expense.from_dict(expense) for expense in json.load(f)]
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    expense_list = [expense.to_dict() for expense in expenses]
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def get_next_id(expenses):
    if not expenses:
        return 1
    return expenses[-1].id + 1

