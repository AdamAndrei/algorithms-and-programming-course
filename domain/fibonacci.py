from time import time


def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    return f(n - 1) * n


# a = time()
# for i in range(999):
#     print(i, f(i))
# b = time()
# print(b - a)
# a = "{}".format(f(998))
# print(len(a), a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])

if 1 in [1, 2, 3]:
    print("a")
else:
    print("b")
