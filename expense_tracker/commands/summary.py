from datetime import datetime
from ..data.repository import ExpenseRepository
from ..utils.formatters import format_currency, format_month_name
from ..utils.validators import ExpenseValidator

class SummaryCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        expenses = self.repo.get_all()
        current_year = datetime.now().year

        if self.args.category:
            expenses = [
                e for e in expenses 
                if e.category.lower() == self.args.category.lower()
            ]
            if self.args.breakdown:
                return self._category_breakdown(expenses)

        if self.args.month:
            ExpenseValidator.validate_month(self.args.month)
            filtered = [
                e for e in expenses
                if e.date.month == self.args.month
                and e.date.year == current_year
            ]
            total = sum(e.amount for e in filtered)
            month_name = format_month_name(self.args.month)
            return f"Total expenses for {month_name}: {format_currency(total)}"
        
        total = sum(e.amount for e in expenses)
        return f"Total expenses: {format_currency(total)}"

    def _category_breakdown(self, expenses):
        categories = {}
        for e in expenses:
            categories[e.category] = categories.get(e.category, 0) + e.amount
        
        lines = ["Category          Amount"]
        for cat, amt in categories.items():
            lines.append(f"{cat:<15}  {format_currency(amt)}")
        return "\n".join(lines)