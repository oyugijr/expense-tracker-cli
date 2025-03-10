from datetime import datetime

from expense_tracker.data.models import Budget
from ..data.repository import ExpenseRepository, BudgetRepository
from ..utils.formatters import format_currency, format_month_name
from ..utils.validators import ExpenseValidator

class SummaryCommand:
    def __init__(self, args):
        self.args = args
        self.expense_repo = ExpenseRepository()
        self.budget_repo = BudgetRepository()

    def execute(self):
        current_year = datetime.now().year
        expenses = self.expense_repo.get_all()
        total = sum(e.amount for e in expenses)
        # total = 0.0
        # target_month = self.args.month


        # Apply filters
        expenses = self._filter_expenses(expenses, current_year)
        
        if self.args.breakdown:
            return self._category_breakdown(expenses)
        
        if self.args.month or self.args.category:
            expenses = self._filter_expenses(expenses, current_year)
            total = sum(e.amount for e in expenses)
            
            if self.args.month:
                month_name = format_month_name(self.args.month)
                budget = self.budget_repo.get_budget(self.args.month, current_year)
            
            if budget:
                return self._format_budget_summary(total, budget, month_name)
            
            else:
                return f"Total expenses for {month_name}: {format_currency(total)}"
        
        return f"Total expenses: {format_currency(total)}"

    def _filter_expenses(self, expenses, current_year):

         # Apply category filter
        if self.args.category:
            expenses = [e for e in expenses 
                        if e.category.lower() == self.args.category.lower()]

        # Then apply month filter        
        if self.args.month:
            ExpenseValidator.validate_month(self.args.month)
            expenses = [e for e in expenses 
                       if e.date.month == self.args.month
                       and e.date.year == current_year]
        
        return expenses

    def _format_budget_summary(self, total, budget, month_name):
        
        base = f"Total expenses for {month_name}: {format_currency(total)}"
        budget_status = f" (Budget: {format_currency(budget.amount)}"

        # if not isinstance(budget, Budget):  # Add type check
        #     raise ValueError("Invalid budget object")
        
        if total > budget.amount:
            over = total - budget.amount
            budget_status += f" ⚠️ Exceeded by {format_currency(over)}"
        elif total > 0.8 * budget.amount:
            budget_status += " ⚠️ Approaching limit"
        else:
            remaining = budget.amount - total
            budget_status += f", Remaining: {format_currency(remaining)}"
            
        return base + budget_status + ")"     

    # def _category_breakdown(self, expenses):
    #     categories = {}
    #     for e in expenses:
    #         categories[e.category] = categories.get(e.category, 0) + e.amount
        
    #     if not categories:
    #         return "No expenses to categorize"
        
    #     max_len = max(len(cat) for cat in categories.keys())
    #     lines = [
    #         f"{'Category':<{max_len}}   Amount",
    #         "-" * (max_len + 15)
    #     ]
        
    #     for cat, amt in sorted(categories.items()):
    #         lines.append(f"{cat:<{max_len}}   {format_currency(amt)}")
        
    #     lines.append("-" * (max_len + 15))
    #     lines.append(f"{'Total':<{max_len}}   {format_currency(sum(categories.values()))}")
        
    #     return "\n".join(lines)

    def _category_breakdown(self, expenses):
        categories = {}
        for e in expenses:
            categories[e.category] = categories.get(e.category, 0) + e.amount
            
        if not categories:
            return "No expenses to categorize"
        
        max_len = max(len(cat) for cat in categories.keys())
        lines = [
             f"{'Category':<{max_len}}   Amount",
                "-" * (max_len + 15)
        ]
                
        for cat, amt in sorted(categories.items()):
            lines.append(f"{cat:<{max_len}}   {format_currency(amt)}")
            total = sum(categories.values())

        lines.append("-" * (max_len + 15))
        lines.append(f"{'Total':<{max_len}}   {format_currency(total)}")

        # Add budget status if month specified
        if self.args.month:
            total = sum(e.amount for e in expenses)
            current_year = datetime.now().year
            budget = self.budget_repo.get_budget(self.args.month, current_year)
            
            if budget:
                utilization = (total / budget.amount) * 100
                status = []
                
                if total > budget.amount:
                    status.append(f"⚠️ Exceeded by {format_currency(total - budget.amount)}")
                elif total > 0.8 * budget.amount:
                    status.append("⚠️ Approaching limit")
                else:
                    status.append(f"Remaining: {format_currency(budget.amount - total)}")
                    
                status.append(f"{utilization:.1f}% utilized")
                lines.append("\nBudget Status:")
                lines.append(f"• Set budget: {format_currency(budget.amount)}")
                lines.append(f"• {', '.join(status)}")

        return "\n".join(lines)