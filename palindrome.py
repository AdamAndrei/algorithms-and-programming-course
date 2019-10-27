def test_is_palindrome():
    assert (is_palindrome(121))
    assert (not is_palindrome(123))
    assert (is_palindrome(323))


def is_palindrome(x):
    ogl = 0
    n = x
    while n > 0:
        ld = n % 10
        ogl = ogl * 10 + ld
        n = n // 10
    if x == ogl:
        return True
    else:
        return False


def main():
    a = int(input("x="))
    if is_palindrome(a):
        print("Numarul  e palindrom")
    else:
        print("Numarul nu  e palindrom")




test_is_palindrome()

main()
"""
def test_is_anti_palindrome():
    assert (test_is_anti_palindrome(1673))
    assert (test_is_anti_palindrome(526379))
    assert (not test_is_anti_palindrome(1668))
    assert (not test_is_anti_palindrome(123326))


def is_anti_palindrome(x):
    k = 0
    n = x
    while n > 0:
        ld = n % 10
        if (ld >= 0):
            k = k + 1
        n = n // 10
    return k

    a = x
    q = 0
    h = k
    for i in range(2, (k // 2) + 1):
        if ((a // (10 ** (i - 1))) % 10) == ((a // (10 ** (k - i))) % 10):
            q = q + 1
    return q

    if q == (h - 2):
        return False
    else:
        return True


def main():
    p = int(input("x="))
    if (is_anti_palindrome(p) == True):
        print("Numarul e antipalindrom")
    else:
        print("Numarul nu e antipalindrom")


main()
"""