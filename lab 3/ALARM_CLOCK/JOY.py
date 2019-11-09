def sum_of_all_divisors(n):
    s = 0
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            s += d
    return s


def all_perfect_numbers():
    z = int(input("asd = "))
    for i in range(200000, z + 1):
        if sum_of_all_divisors(i) == i:
            print(i)


all_perfect_numbers()
