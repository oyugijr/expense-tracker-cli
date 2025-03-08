from datetime import datetime
from expense_tracker.data.models import Budget
from expense_tracker.data.repository import BudgetRepository, ExpenseRepository
from expense_tracker.utils.formatters import format_month_name
from expense_tracker.utils.validators import ExpenseValidator

class SetBudgetCommand:
    def __init__(self, args):
        self.args = args
        self.repo = BudgetRepository()
        self.expense_repo = ExpenseRepository()

    def execute(self):
        ExpenseValidator.validate_month(self.args.month)
        ExpenseValidator.validate_amount(self.args.amount)

        current_year = datetime.now().year
        self.repo.set_budget = Budget(
            month=self.args.month,
            year=current_year,
            amount=self.args.amount
        )
        
        # self.repo.set_budget(budget)
        return f"Budget set for {format_month_name(self.args.month)} {current_year}: {self.args.amount}"

    def set_budget(self, month: int, year: int, amount: float):
        new_budget = Budget(
            month=month,
            year=year,
            amount=amount
        )
        self._budgets = [b for b in self._budgets 
                       if not (b.month == month and b.year == year)]
        self._budgets.append(new_budget)
        self._save_data()