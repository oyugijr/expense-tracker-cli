class ExpenseValidator:
    @staticmethod
    def validate_description(description: str):
        if not description.strip():
            raise ValueError("Description cannot be empty")

    @staticmethod
    def validate_amount(amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    @staticmethod
    def validate_month(month: int):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")

    @staticmethod
    def validate_category(category: str):
        if not category.strip():
            raise ValueError("Category cannot be empty")