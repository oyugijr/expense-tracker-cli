from datetime import date
from ..data.models import Expense
from ..data.repository import ExpenseRepository
from ..data.repository import BudgetRepository
from ..utils.validators import ExpenseValidator
from ..utils.formatters import format_currency, format_month_name
from expense_tracker.data import repository

class AddCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        ExpenseValidator.validate_description(self.args.description)
        ExpenseValidator.validate_amount(self.args.amount)
        ExpenseValidator.validate_category(self.args.category)


        new_expense = Expense(
            id=self.repo.get_next_id(),
            date=date.today(),
            description=self.args.description.strip(),
            amount=self.args.amount,
            category=self.args.category.strip().title()
        )

        self.repo.add(new_expense)
        return f"Expense added successfully (ID: {new_expense.id})"
        self._check_budget(new_expense)

    def _check_budget(self, expense):
        budget_repo = BudgetRepository()
        date = expense.date
        budget = budget_repo.get_budget(date.month, date.year)
        if budget:
            expenses = self.expense_repo.get_all()
            monthly_total = sum(
                e.amount for e in expenses
                if e.date.month == date.month and e.date.year == date.year
            )
        
        if monthly_total > budget.amount:
            over_amount = monthly_total - budget.amount
            over_percent = (over_amount / budget.amount) * 100
            print(f"⚠️  Warning: Exceeded monthly budget by {over_percent:.1f}% (+{format_currency(over_amount)})")