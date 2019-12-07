def rest_suma(s, bancnote):
    # pp banknotes in ascending order
    result = []
    while s != 0:
        chosen = len(bancnote) - 1
        while chosen >= 0 and bancnote[chosen] > s:
            chosen -= 1
        if bancnote[chosen] <= s:
            result.append(bancnote[chosen])
            s -= bancnote[chosen]
        else:
            break
    return result


# print(rest_suma(8, [1, 3, 7]))


def binary_search(needle, haystack):
    st = 0
    dr = len(haystack) - 1
    while st <= dr:
        m = (st + dr) // 2
        # m = st + (st + dr) / 2
        if haystack[m] == needle:
            return True
        if haystack[m] < needle:
            st = m + 1
        else:
            dr = m - 1
    return False


assert binary_search(3, [1, 2, 3]) == True


# assert binary_search(3, [1, 2, 4]) == False
# assert binary_search(0, [1, 2, 3]) == False
# assert binary_search(5, [1, 2, 3]) == False


def expo(a, n):
    if n == 0:
        return 1
    t = expo(a, n // 2)
    if n % 2 == 0:
        return t * t
    return t * t * a


# print(expo(2, 10))


def permutari(n):
    results = []

    def inner(n, permutare_curenta):
        if len(permutare_curenta) == n:
            results.append(permutare_curenta)
            return
        for i in range(1, n + 1):
            if i not in permutare_curenta:
                inner(n, permutare_curenta + [i])

    inner(n, [])
    return results


# for p in permutari(3):
#     print(p)


def permutar(n, k):
    results = []

    def inner(permutare_curenta):
        if len(permutare_curenta) == k:
            results.append(permutare_curenta)
            return
        for i in range(1, n + 1):
            if i not in permutare_curenta:
                inner(permutare_curenta + [i])

    inner([])
    return results


print("")
print("")
print("")

# for p in permutar(5, 3):
#     print(p)

print("")
print("")
print("")
print("")
# for i, a in enumerate(permutar(5, 3)):
#     print(f'{i + 1}.{a}')


def combinari(n, k):

    result = [[1, 0],
              [1, 1, 0]]
    for row in range(2, n+1):
        result.append([1])
        for col in range(1, row + 1):
            result[row].append(result[row - 1][col] + result[row - 1][col - 1])
        result.append(0)
    return result[n][k]

print(combinari(5, 3))
