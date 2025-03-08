import csv
from datetime import datetime
from pathlib import Path
from ..data.repository import ExpenseRepository
from ..utils.formatters import format_currency

class ExportCommand:
    def __init__(self, args):
        self.args = args
        self.repo = ExpenseRepository()

    def execute(self):
        expenses = self._filter_expenses()
        output_path = Path(self.args.output).with_suffix('.csv')
        
        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['ID', 'Date', 'Category', 'Description', 'Amount'])
                
                for expense in expenses:
                    writer.writerow([
                        expense.id,
                        expense.date.isoformat(),
                        expense.category,
                        expense.description,
                        f"{expense.amount:.2f}"
                    ])
                    
            return f"Exported {len(expenses)} expenses to {output_path}"
        except IOError as e:
            raise RuntimeError(f"Failed to write file: {str(e)}")

    def _filter_expenses(self):
        expenses = self.repo.get_all()
        
        # Month filter
        if self.args.month:
            current_year = datetime.now().year
            expenses = [e for e in expenses 
                       if e.date.month == self.args.month
                       and e.date.year == current_year]
        
        # Category filter
        if self.args.category:
            expenses = [e for e in expenses 
                       if e.category.lower() == self.args.category.lower()]
        
        return expenses