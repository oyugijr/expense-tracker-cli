from ..data.repository import ExpenseRepository
from ..utils.validators import ExpenseValidator

class UpdateCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        expense = self.repo.get_by_id(self.args.id)
        if not expense:
            raise ValueError(f"Expense with ID {self.args.id} not found")

        if not self.args.description and self.args.amount is None:
            raise ValueError("Must provide --description or --amount to update")

        if self.args.description:
            ExpenseValidator.validate_description(self.args.description)
            expense.description = self.args.description.strip()

        if self.args.amount is not None:
            ExpenseValidator.validate_amount(self.args.amount)
            expense.amount = self.args.amount

        if not self.repo.update(expense):
            raise ValueError("Failed to update expense")

        return "Expense updated successfully"