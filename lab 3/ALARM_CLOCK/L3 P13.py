
"""
Description:
        -citeste o lista de numere intregi
Out:
        -o lista de numere intregi

"""


def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = int(input("\t x = "))
        lista.append(aux)
    return lista


"""
Description:
        -afiseaza o lista de numere intregi
Out:
        -o lista de numere intregi

"""


def print_list(list):
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


"""
Description:
        -verifica daca un numar este prim
In:
        -numar natural n
Out:
        -True daca e prim,False daca nu e prim
"""


def is_prime(n):
    if n >= 2:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
        return True
    else:
        return False


"""
Description:
        -stabileste daca toate ciferele unui numar sunt numere prime 
In:
        -un numar intreg
Out:
        -True daca toate cifrele sunt numare prime
"""


def prime_digits(n):
    while n > 0:
        ld = n % 10
        if is_prime(ld):
            return True
        else:
            break


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu toate cifrele numre prime
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu toate cifrele numere prime
"""


def subsequence_thirteen(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list)):
        if prime_digits(list[index]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


print_list(subsequence_thirteen(read_list()))


