from ..data.repository import ExpenseRepository
from ..utils.formatters import format_currency

class ListCommand:
    def __init__(self):
        self.repo = ExpenseRepository()

    def execute(self):
        expenses = self.repo.get_all()
        if self.args.category:
            expenses = [e for e in expenses if e.category.lower() == self.args.category.lower()]

        expenses = self.repo.get_all()
        if not expenses:
            return "No expenses found."

        headers = ["ID", "Date", "Category", "Description", "Amount"]
        col_widths = [4, 10, 15, 20, 10]
        
        header = "  ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        rows = [
            f"{str(e.id):<4}  {e.date.isoformat():<10}  {e.description[:20]:<20}  {format_currency(e.amount):>10}"
            for e in expenses
        ]
        
        return "\n".join([header] + rows)