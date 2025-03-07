class SetBudgetCommand:
    def __init__(self, args):
        self.args = args
        self.repo = BudgetRepository()
        self.expense_repo = ExpenseRepository()

    def execute(self):
        ExpenseValidator.validate_month(self.args.month)
        ExpenseValidator.validate_amount(self.args.amount)

        current_year = datetime.now().year
        budget = Budget(
            month=self.args.month,
            year=current_year,
            amount=self.args.amount
        )
        
        self.repo.set_budget(budget)
        return f"Budget set for {format_month_name(self.args.month)} {current_year}"