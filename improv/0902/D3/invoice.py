from dataclasses import dataclass, field



class InvoiceItem:
    ...


class Invoice:
    # items:list[InvoiceItem] = field(default_factory=list)
    # NEBO
    # items:list[dict] = field(default_factory=list)


    def total(self) -> float:
        ...