
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

# def factorial(n):
#     if n == 0: return 1
#     return n * factorial(n-1)

# print(factorial(100))

def merge_sort_basic(slice:list[float]) -> list[float]:
    if len(slice) <= 1:
        return slice[:]
    elif len(slice) == 2:
        if slice[0] <= slice[1]:
            return slice[:]
        else:
            return slice[::-1]
        
    
    # [1, 2, 3, 4, 5] -> [1, 2], [3, 4, 5]
    midpoint = len(slice) // 2
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
        out += r[j:]
        j = len(r)
    elif j >= len(r):
        out += l[i:]
        i = len(l)

    return out


def merge_sort(slice:list[float]) -> list[float]:
    if len(slice) <= 1:
        return slice[:]
    elif len(slice) == 2:
        if slice[0] <= slice[1]:
            return slice[:]
        else:
            return slice[::-1]
        
    midpoint = len(slice) // 2
    l = merge_sort(slice[:midpoint])
    r = merge_sort(slice[midpoint:])        

    l.reverse()
    r.reverse()

    out = []
    while l and r:
        if l[-1] <= r[-1]:
            out.append(l.pop())
        else:
            out.append(r.pop())

        
    if l:
        # l.reverse()
        out.extend(l[::-1])
    elif r:
        # r.reverse()
        out.extend(r[::-1])

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
                out.extend(r[::-1])
                break
            case (x, None):
                out.extend(l[::-1])
                break

            case (x, y) if x <= y:
                out.append(l.pop())
            case (x, y) if x > y:
                out.append(r.pop())

    return out



if __name__ == "__main__":
    from numpy import random
    from timer import timer

    k = random.randint(0, 25000, 5_000_000).tolist()
    # with timer("Naive sort"):
    #     _ = naive_sort(k)

    # k_ = k[:]
    # with timer("Bubble sort"):
    #     bubble_sort(k_)

    with timer("Merge sort I."):
        _ = merge_sort_basic(k)

    with timer("Merge sort II."):
        _ = merge_sort(k)

    # with timer("Merge sort III."):
    #     _ = merge_sort_match(k)











