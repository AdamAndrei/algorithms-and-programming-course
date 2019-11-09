def sum_of_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** 9999
    return s


def limit(x):
    return sum_of_numbers(x) / x ** 10000


for i in range(1, 1000000):
    print(i, limit(i))
