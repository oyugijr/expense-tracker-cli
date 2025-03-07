import json
import os
from typing import List, Optional
from .models import Expense

class ExpenseRepository:
    def __init__(self, file_path='expenses.json'):
        self.file_path = file_path
        self._expenses = self._load_data()

    def _load_data(self) -> List[Expense]:
        if not os.path.exists(self.file_path):
            return []
        
        with open(self.file_path, 'r') as f:
            try:
                data = json.load(f)
                return [Expense.from_dict(item) for item in data]
            except (json.JSONDecodeError, KeyError):
                return []

    def _save_data(self):
        with open(self.file_path, 'w') as f:
            data = [expense.to_dict() for expense in self._expenses]
            json.dump(data, f, indent=2)

    def get_all(self) -> List[Expense]:
        return self._expenses.copy()

    def add(self, expense: Expense):
        self._expenses.append(expense)
        self._save_data()

    def delete(self, expense_id: int) -> bool:
        initial_length = len(self._expenses)
        self._expenses = [e for e in self._expenses if e.id != expense_id]
        if len(self._expenses) < initial_length:
            self._save_data()
            return True
        return False

    def update(self, expense: Expense) -> bool:
        for i, e in enumerate(self._expenses):
            if e.id == expense.id:
                self._expenses[i] = expense
                self._save_data()
                return True
        return False

    def get_next_id(self) -> int:
        if not self._expenses:
            return 1
        return max(e.id for e in self._expenses) + 1

    def get_by_id(self, expense_id: int) -> Optional[Expense]:
        for expense in self._expenses:
            if expense.id == expense_id:
                return expense
        return None