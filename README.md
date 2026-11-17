# mobius-testing

A small invoice-math package used to test Mobius pull request reviews and
GitHub table sync.

```bash
pip install -e '.[test]'
pytest
```

## Usage

```python
from decimal import Decimal
from billing import Invoice, LineItem

inv = Invoice("Acme", tax_rate=Decimal("0.08"))
inv.add(LineItem("Seat", Decimal("25.00"), 3))
print(inv.total)  # 81.00
```

Amounts are `Decimal` and round to whole cents, half up.
