

def _min(l:list[float]) -> float:
    m = None
    for p in l:
        if m is None:
            m = p
        elif p < m:
            m = p

    return m

def _max(l:list[float]) -> float:
    m = None
    for p in l:
        if m is None or p < m:
            m = p
        
    return m

def __max(l:list[float]) -> float:
    _l = [-p for p in l]
    return -_min(_l)

def _druhe_nejvetsi(l:list[float]) -> float:
    m1, m2 = None, None
    for p in l:
        if m1 is None:
            m1 = p
        elif m2 is None or p > m1:
            m2 = p
        elif p > m1:
            m1, m2 = p, m1
        elif p > m2:
            m2 = p

    return m2


def __druhe_nejvetsi(l:list[float]) -> float:
    _l = l[:]
    _m = _max(_l)
    _l.remove(_m)

    return _max(_l)


def _sort(l:list[float]) -> list[float]:
    """Vrátí list se stejnými prvky seřazenými vzestupně"""
    _l = l[:]
    sorted_l = []

    for _ in range(len(l)):
        sorted_l.append(_min(_l))
        _l.remove(sorted_l[-1])

    return sorted_l

def bubble_sort(l:list[float]) -> None:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                sorted = False


def merge_sort(L:list[float]) -> list[float]:
    if len(L) == 2:
        return [L[0], L[1]] if L[0] <= L[1] else [L[1], L[0]]
    
    m = len(L) // 2
    l, r = L[:m], L[m:] # [1, 2, 6, -3, 12, -21, 5, 9] -> [1, 2, 6, -3], [12, -21, 5, 9]

    l = merge_sort(l)
    r = merge_sort(r)


    _l = []

    i, j = 0, 0
    while i < len(l) or j < len(r):
        if i >= len(l): # We used all items from left list
            # for k in range(j, len(r)):
            #     _l.append(r[k])

            _l += r[j:]
            j = len(r)

        
        if j >= len(r): # We used all items from right list
            # for k in range(i, len(l)):
            #     _l.append(l[k])

            _l += l[i:]
            i = len(l)

        
        if i >= len(l) and j >= len(r): # We used all items from both lists
            break

        if l[i] < r[j]:         # If item from left list is smaller
            _l.append(l[i])     #  add it to the result list
            i += 1              #  move to next item in right list
        else:
            _l.append(r[j])     # else, add right item to the result list
            j += 1              #  move to next item in right list


    return _l






if __name__ == "__main__":
    from numpy import random
    from timer import timer

    n = 2**17
    l = random.randint(0, n, n, dtype=int).tolist()

   

    # r2 = l[:]
    # with timer("Bubble sort"):
    #     bubble_sort(r2)

    with timer("Merge sort"):
        r3 = merge_sort(l)

    with timer("Naive sort"):
        r1 = _sort(l)

    print(r1 == r3)