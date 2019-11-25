def sums():
    n = int(input("n= "))
    k = int(input("k = "))
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s += i ** k
        return s % 1.000000007
    return False


print(sums())
