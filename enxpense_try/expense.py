#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import datetime

def load_expenses():
    if not os.path.exists('expenses.json'):
        return []
    try:
        with open('expenses.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=2)

def format_amount(amount):
    if isinstance(amount, float) and amount.is_integer():
        return f"${int(amount)}"
    else:
        return f"${amount:.2f}"

def format_currency(value):
    if isinstance(value, (int, float)) and value.is_integer():
        return f"${int(value)}"
    else:
        return f"${value:.2f}"

def get_total_expenses(expenses, month=None):
    total = 0.0
    current_year = datetime.now().year
    for expense in expenses:
        date = datetime.strptime(expense['date'], "%Y-%m-%d").date()
        if month is not None:
            if date.month == month and date.year == current_year:
                total += expense['amount']
        else:
            total += expense['amount']
    return total

def main():
    parser = argparse.ArgumentParser(prog='expense-tracker')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--amount', type=float, required=True)

    # Delete command
    del_parser = subparsers.add_parser('delete')
    del_parser.add_argument('--id', type=int, required=True)

    # Update command
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('--id', type=int, required=True)
    update_parser.add_argument('--description', required=False)
    update_parser.add_argument('--amount', type=float, required=False)

    # List command
    subparsers.add_parser('list')

    # Summary command
    summary_parser = subparsers.add_parser('summary')
    summary_parser.add_argument('--month', type=int, required=False)

    args = parser.parse_args()

    if args.command == 'add':
        if not args.description.strip():
            print("Error: Description cannot be empty.")
            sys.exit(1)
        if args.amount <= 0:
            print("Error: Amount must be positive.")
            sys.exit(1)
        expenses = load_expenses()
        new_id = max([e['id'] for e in expenses], default=0) + 1
        new_expense = {
            'id': new_id,
            'date': datetime.now().date().isoformat(),
            'description': args.description.strip(),
            'amount': args.amount
        }
        expenses.append(new_expense)
        save_expenses(expenses)
        print(f"Expense added successfully (ID: {new_id})")

    elif args.command == 'delete':
        expense_id = args.id
        expenses = load_expenses()
        new_expenses = [e for e in expenses if e['id'] != expense_id]
        if len(new_expenses) == len(expenses):
            print(f"Error: Expense with ID {expense_id} not found.")
            sys.exit(1)
        save_expenses(new_expenses)
        print("Expense deleted successfully")

    elif args.command == 'update':
        expense_id = args.id
        new_desc = args.description.strip() if args.description else None
        new_amount = args.amount
        if new_desc is None and new_amount is None:
            print("Error: Must provide --description or --amount to update.")
            sys.exit(1)
        if new_amount is not None and new_amount <= 0:
            print("Error: Amount must be positive.")
            sys.exit(1)
        expenses = load_expenses()
        found = False
        for expense in expenses:
            if expense['id'] == expense_id:
                found = True
                if new_desc is not None:
                    expense['description'] = new_desc
                if new_amount is not None:
                    expense['amount'] = new_amount
                break
        if not found:
            print(f"Error: Expense with ID {expense_id} not found.")
            sys.exit(1)
        save_expenses(expenses)
        print("Expense updated successfully")

    elif args.command == 'list':
        expenses = load_expenses()
        if not expenses:
            print("No expenses found.")
            return
        print(f"{'ID':<4}  {'Date':<10}  {'Description':<20}  {'Amount':>10}")
        for expense in expenses:
            amt = format_amount(expense['amount'])
            print(f"{expense['id']:<4}  {expense['date']:<10}  {expense['description']:<20}  {amt:>10}")

    elif args.command == 'summary':
        expenses = load_expenses()
        month = args.month
        if month is not None:
            if month < 1 or month > 12:
                print("Error: Month must be between 1 and 12.")
                sys.exit(1)
            total = get_total_expenses(expenses, month)
            month_name = datetime(1900, month, 1).strftime("%B")
            print(f"Total expenses for {month_name}: {format_currency(total)}")
        else:
            total = sum(e['amount'] for e in expenses)
            print(f"Total expenses: {format_currency(total)}")

if __name__ == '__main__':
    main()