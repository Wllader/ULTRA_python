
def _min(l: list[float]) -> float:
    minimum = l[0]
    for i in l:
        if i < minimum:
            minimum = i
    return minimum


def _sec_min(l: list[float]) -> float:
    a, b = l[0], l[0]
    for i in l:
        if i < a:
            a, b = i, a
        elif i < b:
            b = i
        
    return b


def naive_sort(slice:list[float]) -> list[float]:
    temp = slice[:]
    out = []

    while temp:
        m = _min(temp)
        out.append(m)
        temp.remove(m)

    return out


def bubble_sort(slice:list[float]) -> None:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(slice) - 1):
            if slice[i] > slice[i+1]:
                slice[i], slice[i+1] = slice[i+1], slice[i]
                sorted = False


def merge_sort(slice:list[float]) -> list[float]:
    pass


a = [1, -3, 5, 12, 0, -6, 3, 8]



def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

print(factorial(100))



