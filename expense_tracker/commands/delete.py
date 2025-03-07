from ..data.repository import ExpenseRepository

class DeleteCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        success = self.repo.delete(self.args.id)
        if not success:
            raise ValueError(f"Expense with ID {self.args.id} not found")
        return "Expense deleted successfully"