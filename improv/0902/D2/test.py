

def vypis_pozdrav():
    print("Ahoj!")

def vypis_pozdrav_pro(name:str):
    print(f"Ahoj, {name}!")

def vrat_pozdrav() -> str:
    return "Ahoj!"

def vrat_pozdrav_pro(name:str) -> str:
    return f"Ahoj, {name}!"

def secti(a, b) -> int:
    return a + b

def umocni(base=5, exponent=2) -> int:
    return base**exponent


print(umocni(exponent=3))


