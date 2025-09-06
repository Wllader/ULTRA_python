

def pocitadlo(n=0, max=100):
    print(n)
    if n == max:
        return
    pocitadlo(n+1)


def factorial_rec(n:int):
    if n == 0: return 1
    return n * factorial_rec(n-1)


def factorial_for(n:int):
    p = 1
    for i in range(1, n+1):
        p *= i

    return p


def fibbonacci(n:int):
    pass

