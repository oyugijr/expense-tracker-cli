from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    id: int
    date: date
    description: str
    amount: float
    category: str 

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'description': self.description,
            'amount': self.amount,
            'category': self.category  # Add to serialization
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            date=date.fromisoformat(data['date']),
            description=data['description'],
            amount=data['amount'],
            category=data.get('category', 'Uncategorized')  # Handle existing data
        )