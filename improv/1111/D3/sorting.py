

def _min(l:list[float]) -> tuple[int, float]:
    if not l: raise ValueError("Passed list is empty!")

    minimum_index = 0
    minimum = l[0]
    for i, item in enumerate(l):
        if item < minimum:
            minimum_index, minimum = i, item
    return minimum_index, minimum

def _druhe_nejmensi(l:list[float]) -> float:
    a, b = l[0], l[0]
    for i in l:
        if i < a:
            a, b = i, a
        elif i < b:
            b = i

    return b


def naive_sort(slice:list[float]) -> list[float]:
    tmp = slice[:]
    result = []
    while tmp:
        i, m = _min(tmp)
        tmp.pop(i)
        result.append(m)

    return result


def bubble_sort(slice:list[float]) -> list[float]:
    pass



if __name__ == "__main__":
    l = [1, 3, -8, 6, -3, 12, 0]
    sorted_ = naive_sort(l)
    print(sorted_)