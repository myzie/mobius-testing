from datetime import date
from decimal import Decimal

from billing.late_fees import late_fee

DUE = date(2026, 1, 1)


def test_no_fee_inside_grace():
    assert late_fee(Decimal("200"), DUE, date(2026, 1, 11)) == Decimal("0.00")


def test_first_month_late():
    assert late_fee(Decimal("200"), DUE, date(2026, 1, 12)) == Decimal("3.00")


def test_fee_is_capped():
    assert late_fee(Decimal("200"), DUE, date(2027, 1, 1)) == Decimal("20.00")
