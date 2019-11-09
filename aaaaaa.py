def sum_of_numbers(n):
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    return s


def limit(x):
    return (x ** x) / sum_of_numbers(x)


for i in range(1, 10000):
    print(i, limit(i))

