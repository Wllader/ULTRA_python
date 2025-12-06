

# [1, 5, 8, -3, 2] -> -3
def _min(l:list[float]) -> float:
    if not l: raise ValueError("Passed list is empty!")

    minimum_index = 0
    minimum = l[0]
    for i, n in enumerate(l):
        if n < minimum:
            minimum_index, minimum = i, n
        
    return minimum_index, minimum


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
    tmp = slice[:]
    result = slice[:]
    for i in range(len(result)):
        j, m = _min(tmp)
        tmp.pop(j)
        result[i] = m

    return result



#  [1, 5, 8, -3, 2]
#  [*, *, -3, 8, *]
#  [*, *,  *, 2, 8]
# 
#  [*, -3,  5, *, *]
#  [*,  *,  2, 5, *]
#
#  [-3,  1,  *, *, *]
# =[-3,  1,  2, 5, 8]
def bubble_sort(slice:list[float]) -> None:
    N = len(slice)
    sorted_flag:bool = False
    # for _ in range(N):
    while not sorted_flag:
        sorted_flag = True
        for i in range(N-1):
            if slice[i] > slice[i+1]:
                slice[i], slice[i+1] = slice[i+1], slice[i]
                sorted_flag = False


# def factorial(n:int):
#     if n <= 1: return 1
#     return n * factorial(n-1)


# def factorial(n:int):
#     if n <= 1: return 1
#     p = 1
#     for i in range(1, n+1):
#         p *= i

#     return p


def merge_sort_basic(slice:list[float]) -> list[float]:
    N = len(slice)
    if N <= 1:
        return slice[:]
    elif N == 2:
        return slice[:] if slice[0] <= slice[1] else slice[::-1]
    
    # [1, 5, 8, -3, 2] -> [1, 5], [8, -3, 2]
    midpoint = N // 2
    l = merge_sort_basic(slice[:midpoint])
    r = merge_sort_basic(slice[midpoint:])

    out = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            out.append(l[i])
            i += 1
        else:
            out.append(r[j])
            j += 1

    if i >= len(l):
        out.extend(r[j:])
    elif j >= len(r):
        out.extend(l[i:])

    return out


def merge_sort(slice:list[float]) -> list[float]:
    N = len(slice)
    if N <= 1:
        return slice[:]
    elif N == 2:
        return slice[:] if slice[0] <= slice[1] else slice[::-1]
    
    # [1, 5, 8, -3, 2] -> [1, 5], [8, -3, 2]
    midpoint = N // 2
    l = merge_sort(slice[:midpoint])
    r = merge_sort(slice[midpoint:])

    l.reverse()
    r.reverse()

    out = []
    while l and r:
        out.append(
            l.pop() if l[-1] <= r[-1] else r.pop()
        )

    if l:
        l.reverse()
        out.extend(l)
    elif r:
        r.reverse()
        out.extend(r)

    return out


def merge_sort_match(slice:list[float]) -> list[float]:
    match slice:
        case []:
            return []
        case [x]:
            return [x]
        case [x, y] if x <= y:
            return [x, y]
        case [x, y] if x > y:
            return [y, x]
        
    midpoint = len(slice) // 2
    l = merge_sort_match(slice[:midpoint])
    r = merge_sort_match(slice[midpoint:])

    l.reverse()
    r.reverse()

    out = []
    while l or r:
        match (l[-1] if l else None, r[-1] if r else None):
            case (None, y):
                r.reverse()
                out.extend(r)
                break

            case (x, None):
                l.reverse()
                out.extend(l)
                break

            case (x, y) if x <= y:
                out.append(l.pop())

            case (x, y) if x > y:
                out.append(r.pop())

    return out


if __name__ == "__main__":
    from timer import timer
    from numpy.random import randint
    # l = [1, 3, -8, 6, -3, 12, 0]
    l = randint(0, 25000, 10_000_000).tolist()

    with timer("Merge sort (Basic)"):
        _ = merge_sort_basic(l)

    with timer("Merge sort"):
        _ = merge_sort(l)

    with timer("Merge sort (MatchCase)"):
        _ = merge_sort_match(l)

    # with timer("Naive sort"):
    #     _ = naive_sort(l)

    # with timer("Bubble sort"):
    #     bubble_sort(l)







