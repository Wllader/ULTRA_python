

# [1, 5, 8, -3, 2] -> -3
def _min(l:list[float]) -> float:
    if not l: raise ValueError("Passed list is empty!")

    minimum = l[0]
    for n in l:
        if n < minimum:
            minimum = n
        
    return minimum


# [1, 5, 8, -3, 2] -> 1
def _druhe_min(l:list[float]) -> float:
    if not l: raise ValueError("Passed list is empty!")

    a, b = l[0], l[0]
    for i in l:
        if i < a:
            a, b = i, a
        elif i < b:
            b = i

    return b


def naive_sort(slice:list[float]) -> list[float]:
    "Setřídí slice vzestupně pomocí naší _min funkce."
    pass
