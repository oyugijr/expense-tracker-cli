from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    id: int
    date: date
    description: str
    amount: float

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'description': self.description,
            'amount': self.amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            date=date.fromisoformat(data['date']),
            description=data['description'],
            amount=data['amount']
        )