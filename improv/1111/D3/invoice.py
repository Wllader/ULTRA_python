from dataclasses import dataclass, field



@dataclass
class Invoice:
    #todo
    # Every item has a name, unit, price per unit, count
    items:list = field(default_factory=list)

    def total(self) -> float:
        pass

    def add_item(self, ...):
        pass

    def add_items(self, ...):
        pass


# def foo(l:list[str] = None):
#     l = l or list()
#     l.append("Ahoj!")
#     return l


# k = foo()
# print(k)
# k = foo()

# print(k)