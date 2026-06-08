import argparse
import datetime
from expense_tracker import storage
from expense_tracker.expense import Expense

def build_parser():

    parser = argparse.ArgumentParser(
        prog='expense-tracker',
        description='Track, update, or delete your expenses',
        epilog='Thank you for using expense-tracker!'
    )

    subparser = parser.add_subparsers(dest='command')

    add_parser = subparser.add_parser('add', help='Add an expense')
    add_parser.add_argument('title', help='Title/Name of the expense', type=str)
    add_parser.add_argument('description', help='Description of the expense', type=str)
    add_parser.add_argument('amount', help='Amount of the expense', type=float)
    add_parser.set_defaults(func=add_expense)

    update_parser = subparser.add_parser('update', help='Update an existing expense')
    update_parser.add_argument('id', help='ID of the expense', type=int)
    update_parser.add_argument('--title', help='Title of the expense', type=str)
    update_parser.add_argument('--description', help='Description of the expense', type=str)
    update_parser.add_argument('--amount', help='Amount of the expense', type=float)
    update_parser.add_argument('--month', help='Month of the expense', type=int)
    update_parser.set_defaults(func=update_expense)

    delete_parser = subparser.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('id', help='ID of the expense', type=int)
    delete_parser.set_defaults(func=delete_expense)

    view_parser = subparser.add_parser('view', help='View expenses')
    view_parser.set_defaults(func=view_expenses)

    summary_parser = subparser.add_parser('summary', help='Show expenses summary')
    summary_parser.add_argument('--month', help='Month of expenses to summarize (1-12)', type=int)
    summary_parser.set_defaults(func=summarize_expenses)

def add_expense(args):
    expenses = storage.read_expenses()
    new_id = storage.get_next_id(expenses)
    date = datetime.datetime.now().month
    new_expense = Expense(new_id, args.title, args.description, args.amount, date)

    expenses.append(new_expense)
    storage.save_expenses(expenses)
    print(f"Added expense '{args.title}' to expense tracker.")

def update_expense(args):
    expenses = storage.read_expenses()
    found = False
    updated = False
    for expense in expenses:
        if expense.id == args.id:
            if args.title is not None:
                expense.title = args.title
                updated = True
            if args.description is not None:
                expense.description = args.description
                updated = True
            if args.amount is not None:
                expense.amount = args.amount
                updated = True
            found = True
    if not found:
        print(f"No expense with id {args.id} found.")
    elif not updated:
        print("Nothing was updated")
    else:
        storage.save_expenses(expenses)
        print(f"Updated expense '{args.id}' successfully.")


def delete_expense(args):
    expenses = storage.read_expenses()
    expenses_length = len(expenses)
    expenses = [expense for expense in expenses if expense.id != args.id]
    if len(expenses) < expenses_length:
        storage.save_expenses(expenses)
        print(f"Expense {args.id} deleted successfully.")
    else:
        print(f"Expense {args.id} could not be found.")

def view_expenses(args):
    expenses = storage.read_expenses()
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(expense)

def summarize_expenses(args):
    expenses = storage.read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    if args.date is not None:
        filtered = [expense for expense in expenses if expense.date == args.date]
        if not filtered:
            print(f"No expenses found for month {args.date}.")
            return
        total = sum(expense.amount for expense in filtered)
        print(f"Total expenses for month {args.date}: ${total:.2f}")
    else:
        total = sum(expense.amount for expense in expenses)
        print(f"Total expenses: ${total:.2f}")
