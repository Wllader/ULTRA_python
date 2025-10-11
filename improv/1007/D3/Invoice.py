from dataclasses import dataclass, field

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
    items:list[InvoiceItem] = field(default_factory=list)

    def total(self) -> float:
        "Vrátí součet všech položek faktury"
        running_total = 0
        for item in self.items:
            running_total += item.total()

        return running_total
    
    def total(self) -> float:
        return sum(( item.total() for item in self.items ))

    def add_item(self, item:InvoiceItem):
        self.items.append(item)

    def add_items(self, items:list[InvoiceItem]):
        for item in items:
            self.add_item(item)

    @staticmethod
    def fromItems(*items:list[InvoiceItem]) -> "Invoice":
        invoice = Invoice()
        invoice.add_items(items)
        return invoice


if __name__ == "__main__":
    names =     ["jablko", "pomeranč", "banán"]
    units =     ["ks", "ks", "ks"]
    ppus =      [23, 28.5, 39.9]
    counts =    [6, 3, 2]

    items = zip(names, units, ppus, counts)
    items = ( InvoiceItem(*item) for item in items)

    invoice = Invoice.fromItems(*items)
    print(
        invoice,
        invoice.total(),

        sep="\n"
    )