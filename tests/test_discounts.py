from decimal import Decimal

from billing import Invoice, LineItem
from billing.discounts import Discount, discounted_total


def test_ten_percent_off():
    inv = Invoice("Acme")
    inv.add(LineItem("Seat", Decimal("100.00")))
    assert discounted_total(inv, Discount("SAVE10", Decimal("10"))) == Decimal("90.00")
