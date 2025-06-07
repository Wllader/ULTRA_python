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
    items:list[Invoice_Item] = field(default_factory=list)

    def total(self):
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


itm1 = Invoice_Item("jablko", "ks", 23, 6)
itm2 = Invoice_Item("pomeranč", "ks", 28, 3)
itm3 = Invoice_Item("banány", "ks", 38, 2)

invoice = Invoice.fromItems(itm1, itm2, itm3)


print(
    invoice,
    invoice.total()
)