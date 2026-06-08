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

def add_expense(args):
    return

def update_expense(args):