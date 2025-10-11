from dataclasses import dataclass, field

@dataclass
class Invoice:
    items:...

    def total(self) -> float:
        "Vrátí součet všech položek faktury"
        ...

    def add_item(self, item:...):
        ...

    def add_items(self, items:...):
        ...

    @staticmethod
    def fromItems(items:...) -> "Invoice":
        ...


if __name__ == "__main__":
    i = Invoice()
    j = Invoice()

    i.items.append(5)
    print(i, j)