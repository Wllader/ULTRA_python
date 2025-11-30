import numpy as np

def bound(y:float, lower_bound:int, upper_bound:int) -> float:
    span = upper_bound - lower_bound

    pos = (y - lower_bound) % (2*span)
    if pos > span:
        pos = 2*span - pos

    return pos + lower_bound

def _bound(y:float, lower_bound:int, upper_bound:int) -> float:
    "This implementation is inefficient!"
    if y >= lower_bound and y <= upper_bound:
        return y
    
    if y < lower_bound:
        y0 = np.abs(lower_bound - y)
        return _bound(y + 2*y0, lower_bound, upper_bound)
    
    if y > upper_bound:
        y0 = np.abs(upper_bound - y)
        return _bound(y - 2*y0, lower_bound, upper_bound)



if __name__ == "__main__":
    numbers = [5, 8, 12, -6, 9, 3]
    bounds = [(0, 5), (5, 10), (-5, 0), (-10, -5)]

    for n in numbers:
        for l, u in bounds:
            print(f"{_bound(n, l, u) == bound(n, l, u)=}")