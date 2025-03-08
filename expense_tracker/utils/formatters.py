from datetime import datetime

def format_currency(amount: float) -> str:
    if isinstance(amount, float) and amount.is_integer():
        return f"${int(amount)}"
    return f"${amount:.2f}"

def format_month_name(month: int) -> str:
    return datetime(1900, month, 1).strftime("%B")

def format_date(date_str: str) -> str:
    """Convert ISO date to YYYY-MM-DD format"""
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")