# from ..data.repository import ExpenseRepository
# from ..utils.formatters import format_currency, format_date

# class ListCommand:
#     def __init__(self):
#         self.repo = ExpenseRepository()

#     def execute(self):
#         expenses = self.repo.get_all()
#         if not expenses:
#             return "No expenses found."

#         headers = ["ID", "Date", "Description", "Amount"]
#         rows = [
#             [
#                 str(e.id),
#                 format_date(e.date.isoformat()),
#                 e.description,
#                 format_currency(e.amount)
#             ] for e in expenses
#         ]

#         # Format table
#         col_widths = [4, 10, 20, 10]
#         header_line = "  ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
#         lines = [header_line]
#         for row in rows:
#             lines.append("  ".join(f"{col:<{w}}" for col, w in zip(row, col_widths)))
        
#         return "\n".join(lines)

from ..data.repository import ExpenseRepository
from ..utils.formatters import format_currency

class ListCommand:
    def __init__(self):
        self.repo = ExpenseRepository()

    def execute(self):
        expenses = self.repo.get_all()
        if not expenses:
            return "No expenses found."

        headers = ["ID", "Date", "Description", "Amount"]
        col_widths = [4, 10, 20, 10]
        
        header = "  ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
        rows = [
            f"{str(e.id):<4}  {e.date.isoformat():<10}  {e.description[:20]:<20}  {format_currency(e.amount):>10}"
            for e in expenses
        ]
        
        return "\n".join([header] + rows)