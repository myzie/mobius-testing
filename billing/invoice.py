from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def to_money(value: Decimal) -> Decimal:
    """Round to whole cents, half up, the way customers expect."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class LineItem:
    description: str
    unit_price: Decimal
    quantity: int = 1

    def __post_init__(self) -> None:
        if self.quantity < 1:
            raise ValueError("quantity must be at least 1")
        if self.unit_price < 0:
            raise ValueError("unit_price cannot be negative")

    @property
    def amount(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass
class Invoice:
    customer: str
    tax_rate: Decimal = Decimal("0")
    items: list[LineItem] = field(default_factory=list)

    def add(self, item: LineItem) -> None:
        self.items.append(item)

    @property
    def subtotal(self) -> Decimal:
        return to_money(sum((i.amount for i in self.items), Decimal("0")))

    @property
    def tax(self) -> Decimal:
        return to_money(self.subtotal * self.tax_rate)

    @property
    def total(self) -> Decimal:
        return self.subtotal + self.tax
