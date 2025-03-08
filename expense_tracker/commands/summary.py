from datetime import datetime
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
        total = 0.0
        target_month = self.args.month

        if target_month:
            ExpenseValidator.validate_month(target_month)
            filtered_expenses = [
                e for e in expenses
                if e.date.month == target_month
                and e.date.year == current_year
            ]
            total = sum(e.amount for e in filtered_expenses)
            month_name = format_month_name(target_month)
            budget = self.budget_repo.get_budget(target_month, current_year)

            if budget:
                return self._format_budget_summary(total, budget, month_name)
                return f"Total expenses for {month_name}: {format_currency(total)}"

                total = sum(e.amount for e in expenses)
                return f"Total expenses: {format_currency(total)}"

    def _format_budget_summary(self, total, budget, month_name):
        base = f"Total expenses for {month_name}: {format_currency(total)}"
        budget_status = f" (Budget: {format_currency(budget.amount)}"
        
        if total > budget.amount:
            over = total - budget.amount
            budget_status += f" ⚠️ Exceeded by {format_currency(over)}"
        elif total > 0.8 * budget.amount:
            budget_status += " ⚠️ Approaching limit"
        else:
            remaining = budget.amount - total
            budget_status += f", Remaining: {format_currency(remaining)}"
            
        return base + budget_status + ")"            

    #     if budget := self.budget_repo.get_budget(target_month, current_year):
    #         budget_status = f" (Budget: {format_currency(budget.amount)}"
    #     if total > budget.amount:
    #         budget_status += f" ⚠️ Exceeded by {format_currency(total - budget.amount)}"
    #     elif total > 0.8 * budget.amount:
    #         budget_status += " ⚠️ Approaching limit"
    #     print(budget_status)

    #     if self.args.category:
    #         expenses = [
    #             e for e in expenses 
    #             if e.category.lower() == self.args.category.lower()
    #         ]
    #         if self.args.breakdown:
    #             return self._category_breakdown(expenses)

    #     if self.args.month:
    #         ExpenseValidator.validate_month(self.args.month)
    #         filtered = [
    #             e for e in expenses
    #             if e.date.month == self.args.month
    #             and e.date.year == current_year
    #         ]
    #         total = sum(e.amount for e in filtered)
    #         month_name = format_month_name(self.args.month)
    #         return f"Total expenses for {month_name}: {format_currency(total)}"
        
    #     total = sum(e.amount for e in expenses)
    #     return f"Total expenses: {format_currency(total)}"

    # def _category_breakdown(self, expenses):
    #     categories = {}
    #     for e in expenses:
    #         categories[e.category] = categories.get(e.category, 0) + e.amount
        
    #     lines = ["Category          Amount"]
    #     for cat, amt in categories.items():
    #         lines.append(f"{cat:<15}  {format_currency(amt)}")
    #     return "\n".join(lines)