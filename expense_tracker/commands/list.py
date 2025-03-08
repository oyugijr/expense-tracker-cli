from datetime import datetime
from ..data.repository import ExpenseRepository
from ..utils.formatters import format_currency, format_date

class ListCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        expenses = self.repo.get_all()
        current_year = datetime.now().year

        # Apply filters
        if self.args.month:
            expenses = [e for e in expenses 
                        if e.date.month == self.args.month
                        and e.date.year == current_year]
            
        if self.args.category:
            expenses = [e for e in expenses
                        if e.category.lower() == self.args.category.lower()]

        # expenses = self.repo.get_all()
        if not expenses:
            return "No expenses found."
        
         # Calculate dynamic column widths
        max_category = max(len(e.category) for e in expenses) if expenses else 8
        max_desc = max(len(e.description) for e in expenses) if expenses else 20
        
        col_widths = {
            'id': 4,
            'date': 10,
            'category': max(8, max_category),
            'description': max(20, max_desc),
            'amount': 10
        }

        # Build header
        header = (
            f"{'ID':<{col_widths['id']}}  "
            f"{'Date':<{col_widths['date']}}  "
            f"{'Category':<{col_widths['category']}}  "
            f"{'Description':<{col_widths['description']}}  "
            f"{'Amount':>{col_widths['amount']}}"
        )

        # Build rows
        rows = []
        for e in expenses:
            rows.append(
                f"{e.id:<{col_widths['id']}}  "
                f"{format_date(e.date.isoformat()):<{col_widths['date']}}  "
                f"{e.category:<{col_widths['category']}}  "
                f"{e.description[:col_widths['description']]:<{col_widths['description']}}  "
                f"{format_currency(e.amount):>{col_widths['amount']}}"
            )

        return "\n".join([header] + rows)

        # headers = ["ID", "Date", "Category", "Description", "Amount"]
        # col_widths = [4, 10, 15, 30, 10]
        
        # header = "  ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        # rows = [
        #     f"{str(e.id):<4}  {e.date.isoformat():<10}  {e.description[:20]:<20}  {format_currency(e.amount):>10}"
        #     for e in expenses
        # ]
        
        # return "\n".join([header] + rows)