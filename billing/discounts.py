from dataclasses import dataclass
from decimal import Decimal

from billing.invoice import Invoice, to_money


@dataclass(frozen=True)
class Discount:
    code: str
    percent: Decimal  # 10 means 10% off


def discounted_total(invoice: Invoice, discount: Discount) -> Decimal:
    """The invoice total after a percentage discount code."""
    off = invoice.total * discount.percent / 100
    return to_money(invoice.total - off)
