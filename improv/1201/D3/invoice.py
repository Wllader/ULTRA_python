from dataclasses import dataclass, field
from typing import Iterable, Self


@dataclass
class InvoiceItem:
    name:str
    unit:str
    price_per_unit:float
    unit_count:float

    def total(self) -> float:
        return self.price_per_unit * self.unit_count

@dataclass
class Invoice:
    # Every item has a name, unit, price per unit, count
    items:list[InvoiceItem] = field(default_factory=list)

    def total(self) -> float:
        running_total = 0
        for item in self.items:
            running_total += item.total()

        return running_total
    
    def total(self) -> float:
        return sum(( item.total() for item in self.items ))

    def add_item(self, item:InvoiceItem) -> Self:
        self.items.append(item)
        return self

    def add_items(self, items:Iterable[InvoiceItem]) -> Self:
        for item in items:
            self.items.append(item)
        return self

    @staticmethod
    def fromItems(items:Iterable[InvoiceItem]):
        return Invoice().add_items(items)
    

if __name__ == "__main__":
    names =     ["jablko", "mouka", "malování pokojů"]
    units =     ["ks", "kg", "h"]
    ppus  =     [23, 16, 350]
    counts =    [6, 5, 4.25]

    items = zip(names, units, ppus, counts)
    items = ( InvoiceItem(*item) for item in items )

    invoice = Invoice.fromItems(items)
    print(
        invoice,
        invoice.total(),

        sep="\n--\n"
    )