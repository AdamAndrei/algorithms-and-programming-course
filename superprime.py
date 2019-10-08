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


def is_super_prime(number):
    prefix = number
    while prefix > 0:
        if not is_prime(prefix):
            return False
        prefix = prefix // 10
    return True


def test_is_superprim():
    assert (is_super_prime(233))
    assert (is_super_prime(23))
    assert (not is_super_prime(234))


def main():
    a = int(input("x="))
    if is_super_prime(a):
        print("Este superprim")
    else:
        print("Nu este superprim")


test_is_superprim()
main()
