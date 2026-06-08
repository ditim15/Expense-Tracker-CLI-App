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
    month = datetime.datetime.now().month
    new_expense = Expense(new_id, args.title, args.description, args.amount, month)

    expenses.append(new_expense)
    storage.save_expenses(expenses)
    print(f"Added expense '{args.title}' to expense tracker.")

def update_expense(args):
    return

def delete_expense(args):
    return

def view_expenses(args):
    return

def summarize_expenses(args):
    return