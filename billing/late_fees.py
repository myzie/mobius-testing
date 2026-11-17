from datetime import date
from decimal import Decimal

from billing.invoice import to_money

GRACE_DAYS = 10
MONTHLY_RATE = Decimal("0.015")  # 1.5% per started month past grace
MAX_FEE_RATE = Decimal("0.10")  # never more than 10% of the balance


def late_fee(balance: Decimal, due: date, today: date) -> Decimal:
    """The late fee owed on an unpaid balance."""
    days_late = (today - due).days - GRACE_DAYS
    if days_late <= 0 or balance <= 0:
        return Decimal("0.00")
    months = -(-days_late // 30)  # each started month counts
    fee = balance * MONTHLY_RATE * months
    return to_money(min(fee, balance * MAX_FEE_RATE))
