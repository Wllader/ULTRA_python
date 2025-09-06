

def _min(slice:list[float]) -> float:
    if not slice:
        return None
    
    m = slice[0]

    for p in slice:
        if p < m:
            m = p

    return m

# [1, 5, -6, 3] -> [-6, 1, 3, 5]


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
            if slice[i] > slice[i + 1]:
                slice[i], slice[i+1] = slice[i+1], slice[i]
                sorted = False


def merge_sort1(slice:list[float]) -> list[float]:
    if len(slice) <= 1:
        return slice[:]
    elif len(slice) == 2:
        if slice[0] <= slice[1]:
            return slice[:]
        else:
            return slice[::-1]
        
    
    midpoint = len(slice) // 2
    l = merge_sort1(slice[:midpoint])
    r = merge_sort1(slice[midpoint:])

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


def merge_sort2(slice:list[float]) -> list[float]:
    if len(slice) <= 1:
        return slice[:]
    elif len(slice) == 2:
        if slice[0] <= slice[1]:
            return slice[:]
        else:
            return slice[::-1]
        
    midpoint = len(slice) // 2
    l = merge_sort2(slice[:midpoint])
    r = merge_sort2(slice[midpoint:])

    l.reverse()
    r.reverse()

    out = []
    while l and r:
        if l[-1] <= r[-1]:
            out.append(l.pop())
        else:
            out.append(r.pop())

    if l:
        l.reverse()
        out.extend(l)
    elif r:
        r.reverse()
        out.extend(r)

    return out


def merge_sort3(slice:list[float]) -> list[float]:
    match slice:
        case []:
            return []
        case [x]:
            return slice[:]
        case [x, y] if x <= y:
            return slice[:]
        case [x, y] if x > y:
            return [y, x]
        
    midpoint = len(slice) // 2
    l = merge_sort3(slice[:midpoint])
    r = merge_sort3(slice[midpoint:])

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
    from numpy import random
    k = random.randint(0, 25000, 10_000_000).tolist()


    # with timer("Naive sort"):
    #     _ = naive_sort(k)

    # k_ = k[:]
    # with timer("Bubble sort"):
    #     bubble_sort(k_)

    with timer("Merge sort I."):
        _ = merge_sort1(k)

    with timer("Merge sort II."):
        _ = merge_sort2(k)

    with timer("Merge sort III."):
        _ = merge_sort3(k)
