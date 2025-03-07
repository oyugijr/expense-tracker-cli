from datetime import date
from ..data.models import Expense
from ..data.repository import ExpenseRepository
from ..utils.validators import ExpenseValidator

class AddCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        ExpenseValidator.validate_description(self.args.description)
        ExpenseValidator.validate_amount(self.args.amount)

        new_expense = Expense(
            id=self.repo.get_next_id(),
            date=date.today(),
            description=self.args.description.strip(),
            amount=self.args.amount
        )

        self.repo.add(new_expense)
        return f"Expense added successfully (ID: {new_expense.id})"