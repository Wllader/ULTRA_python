from dataclasses import dataclass, field


@dataclass
class Invoice_Item:
    name:str
    unit:str
    price_per_unit:float
    unit_count:float

    def total(self) -> float:
        return self.price_per_unit * self.unit_count


@dataclass
class Invoice:
    #Item (name, unit, ppu, count)
    items:list[Invoice_Item] = field(default_factory=list)
    

    def total(self) -> float:
        running_total = 0
        for item in self.items:
            running_total += item.total()

        return running_total
    
    def add_item(self, item:Invoice_Item) -> None:
        self.items.append(item)

    def add_items(self, items:list[Invoice_Item]) -> None:
        for item in items:
            self.add_item(item)

    
    @staticmethod
    def fromItems(*items:list[Invoice_Item]) -> "Invoice":
        invoice = Invoice()
        invoice.add_items(items)

        return invoice




if __name__ == "__main__":
    names = ["jablko", "pomeranč", "banán"]
    units = ["ks", "ks", "ks"]
    ppus = [23, 28, 38]
    counts = [6, 3, 2]

    items = list(zip(names, units, ppus, counts))
    items = [ Invoice_Item(*item) for item in items ]

    invoice = Invoice.fromItems(*items)

    print(
        invoice,
        invoice.total()
    )