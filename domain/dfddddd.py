def count_stairs(n):
    if n == 0:
        return 0
    if 1 == n:
        return 1
    if 2 == n:
        return 2

    return count_stairs(n - 1) + count_stairs(n - 2)

n = 10000

# print(count_stairs(100))

a = 1
for i in range(1, 1000):
    a += 1 / (2 ** i)
    print(i, 5 * a)
