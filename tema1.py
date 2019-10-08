def isprime(n):
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


def testisprime():
    assert (isprime(7) == True)


def run():
    testisprime()
    x = int(input("x="))
    af = isprime(x)
    for i in range(1, x):
        if isprime(i):
            print(i)


run()
