a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print filter(lambda x: x % 2 == 0, a)


def fun_filter(num):
    return num % 2 == 0

print filter(fun_filter, a)
