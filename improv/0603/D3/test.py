from dataclasses import dataclass

# l = list("asdflki")

# print(*l)

# for item in l:
#     print(item, end=" ")
# print()

@dataclass
class C:
    _value:int

    @property
    def value(self):
        print(f"Čtení {self}")
        return self._value
    
    @value.setter
    def value(self, val):
        print(f"Zápis do {self}")
        self._value = val


c = C(5)
print(c.value)
c.value = 9
print(c.value)

c.value = -6
print(c.value)