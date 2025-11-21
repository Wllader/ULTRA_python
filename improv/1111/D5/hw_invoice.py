from dataclasses import dataclass, field
from typing import Iterable

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
    #todo
    # Every item has a name, unit, price per unit, count
    items:list[InvoiceItem] = field(default_factory=list)

    def total(self) -> float:
        "Vrátí součet všech položek faktury"
        running_total = 0
        for item in self.items:
            running_total += item.total()

    def total(self) -> float:
        return sum(( item.total() for item in self.items ))

    def add_item(self, item:InvoiceItem) -> "Invoice":
        self.items.append(item)
        return self

    def add_items(self, items:Iterable[InvoiceItem]) -> "Invoice":
        for item in items:
            self.add_item(item)

        return self

    @staticmethod
    def fromItems(items:Iterable[InvoiceItem]):
        return Invoice().add_items(items)


if __name__ == "__main__":
    names =     ["jablko", "mouka", "malování pokojů"]
    units =     ["ks",  "kg",   "h"]
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


# def foo(l:list[str] = None):
#     l = l or list()
#     l.append("Ahoj!")
#     return l


# k = foo()
# print(k)
# k = foo()

# print(k)