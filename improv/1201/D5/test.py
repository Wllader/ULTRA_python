


def foo(l:list[int] = None):
    _l = l if l is not None else list()
    _l.append(999)
    return _l


if __name__ == "__main__":


    k = foo([1, 2, 3])
    print(k)

    q = foo([5, 6, 7])
    print(q)
