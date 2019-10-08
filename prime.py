def is_prime(n):
    # descriere:verifica daca un numar este prim
    # in:un  numar natural n
    # out:True daca e prim,False daca nu e prim
    if n >= 2:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
        return True
    else:
        return False


def test_is_prime():
    assert (is_prime(7))
    assert (is_prime(2))
    assert (not is_prime(1))
    assert (not is_prime(8))
    assert (not is_prime(15))


def run_using_while(x):
    i = x - 1
    found_prime = False
    while i >= 2 and found_prime == False:
        if is_prime(i):
            found_prime = True
            print(i)

        i -= 1


def main():
    x = int(input("x="))

    run_using_while(x)


test_is_prime()

main()
