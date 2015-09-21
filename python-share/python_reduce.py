a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print reduce(lambda x, y: x + y, a)


def add(x, y):
    return x + y

print reduce(add, a)
