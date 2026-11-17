from decimal import Decimal

import pytest

from billing import Invoice, LineItem


def test_totals_with_tax():
    inv = Invoice("Acme", tax_rate=Decimal("0.08"))
    inv.add(LineItem("Seat", Decimal("25.00"), 3))
    inv.add(LineItem("Onboarding", Decimal("99.99")))
    assert inv.subtotal == Decimal("174.99")
    assert inv.tax == Decimal("14.00")
    assert inv.total == Decimal("188.99")


def test_empty_invoice_is_zero():
    assert Invoice("Acme").total == Decimal("0.00")


@pytest.mark.parametrize("qty", [0, -1])
def test_rejects_bad_quantity(qty):
    with pytest.raises(ValueError):
        LineItem("Seat", Decimal("25.00"), qty)
