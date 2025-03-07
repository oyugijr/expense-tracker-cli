from datetime import datetime

def format_currency(amount: float) -> str:
    if isinstance(amount, float) and amount.is_integer():
        return f"${int(amount)}"
    return f"${amount:.2f}"

def format_month_name(month: int) -> str:
    return datetime(1900, month, 1).strftime("%B")