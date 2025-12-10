from dataclasses import dataclass, field
from typing import Iterable



@dataclass
class Invoice:
    # Every item has a name, unit, price per unit, count
    items:list = field(default_factory=list)

    def total(self) -> float: ...


    def add_item(...): pass

    def add_items(self, items:Iterable[...]): pass


    @staticmethod
    def fromItems(...): pass