
def _min(l:list[float]) -> float:
    """Vrátí nejmenší prvek z daného listu"""
    m = None
    for p in l:
        if m == None:
            m = p
        elif p < m:
            m = p
    
    return m

def _max(l:list[float]) -> float:
    """Vrátí největší prvek z daného listu"""
    m = None
    for p in l:
        if m == None:
            m = p
        elif p > m:
            m = p
    
    return m

def __max(l:list[float]) -> float:
    _l = [-p for p in l]
    return -_min(_l)

def _druhe_nejvetsi(l:list[float]) -> float:
    """Vrátí druhý největší prvek z daného listu"""
    _l = l[:]
    _m = _max(_l)
    _l.remove(_m)
    return _max(_l)

def _sort(l:list[float]) -> list[float]:
    """Vrátí list se stejnými prvky seřazenými vzestupně"""
    _l = l[:]
    m = []
    for _ in range(len(l)):
        m.append(_min(_l))
        _l.remove(m[-1])

    return m

def merge_sort(L:list[float]) -> list[float]:
    if len(L) == 2:
        return [L[0], L[1]] if L[0] < L[1] else [L[1], L[0]]

    m = len(L) // 2
    l, r = L[:m], L[m:] # [1, 2, 6, -3, 12, -21, 5, 9] -> [1, 2, 6, -3], [12, -21, 5, 9]
    l = merge_sort(l)
    r = merge_sort(r)

    _l = []

    i, j = 0, 0
    while i < len(r) or j < len(l):
        if i >= len(r):
            for k in range(j, len(l)):
                _l.append(l[k])
            j = len(l)

        if j >= len(l):
            for k in range(i, len(r)):
                _l.append(r[k])
            i = len(r)

        if i >= len(r) and j >= len(l):
            break

        if r[i] < l[j]:
            _l.append(r[i])
            i += 1
        else:
            _l.append(l[j])
            j += 1

    return _l
        
# l = [1, 2, 6, -3, 12, -21, 5, 9]

# print(
#     _min(l),
#     _max(l),
#     __max(l),
#     _druhe_nejvetsi(l),
#     _sort(l),
#     merge_sort(l),

#     sep="\n"
# )


import numpy as np
from time import perf_counter as pc

l1 = np.random.randint(0, 1000, 2**15).tolist()
l2 = l1[:]

start_time = pc()
s1 = _sort(l1)
t1 = pc() - start_time
print(f"Naivní sort trval {t1}")

start_time = pc()
s2 = merge_sort(l2)
t2 = pc() - start_time
print(f"Merge-sort trval {t2}")

print(s1 == s2)
print(f"Merge-sort je {t1/t2:.5f}x efektivnější")

