import time


def factorial(m):
    a = 1
    if m > 0:
        for i in range(1, m + 1):
            a = a * i
    else:
        a = 1
    return a


def number_of_steps(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 0:
        return 0
    else:
        if n % 2 == 0:
            a = 0
            for i in range(n - 2, (n // 2), -1):
                a += factorial(i) // (factorial(n - i) * factorial((2 * i) - n))
            a += n + 1
            return a
        else:
            b = 0
            for i in range(n - 2, (n // 2), -1):
                b += factorial(i) // (factorial(n - i) * factorial((2 * i) - n))
            b += n
            return b


def fibonacci(n):
    prev = 1
    current = 2
    for i in range(3, n + 1):
        old_current = current
        current = current + prev
        prev = old_current

    return current


def number_of_digits(n):
    a = 0
    while n > 0:
        a += 1
        n = n // 10
    return a

for i in range (2, 100):
    print(i, "  ", number_of_steps(i), "  ", number_of_steps(i - 1), "   ", number_of_steps(i) / number_of_steps(i - 1))

#
# for k in range(2, 10000):
#     print(k, number_of_digits(fibonacci(k)))
#     # print(k, "  ", fibonacci(k), "  ", fibonacci(k - 1), "   ", fibonacci(k) / fibonacci(k - 1))
#
#
# # print(number_of_digits(number_of_steps(10000)))
#
# def benchmark(fuctionName, n):
#     start_time = time.time()
#     print(fuctionName)
#     print(fuctionName(n))
#     print("Duration: {}".format(time.time() - start_time))
#
#
# # n = 2500
# # benchmark(fibonacci, n)
# # benchmark(number_of_steps, n)
