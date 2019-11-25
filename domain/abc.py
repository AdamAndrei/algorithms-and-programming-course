def factorial(m):
    a = 1
    if m > 0:
        for i in range(1, m + 1):
            a = a * i
    else:
        a = 1
    return a


def list_of_digits(a):
    list = []
    while a > 0:
        n = a % 10
        list.append(n)
        a = a // 10
    return list


def sum(q):
    b = 0
    for i in range(len(list_of_digits(q))):
        b += factorial(list_of_digits(q)[i])
    if b == q:
        print(q)


for i in range(1, 100000):
    sum(i)

