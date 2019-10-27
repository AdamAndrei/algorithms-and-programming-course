def two_base(a):
    m = 0
    p = 1
    while a > 0:
        r = a % 2
        m = m + (r * p)
        p = p * 10
        a = a // 2
    return m


def bits(Number):
    a = two_base(Number)
    number_of_one = 0
    while a > 0:
        ld = a % 10
        if ld == 1:
            number_of_one += 1
        a = a // 10
    return number_of_one


def read_list():
    n = int(input("Number of elements=  "))
    lista = []

    for index in range(n):
        aux = int(input("\t x = "))
        lista.append(aux)
    return lista


def print_list(list):
    length = len(list)
    for index in range(length):
        if index == (length - 1):
            print(list[index], "\n")
        else:
            print(list[index], end=" , ")


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
"""


def subsequence_eleven(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
        if bits(list[index]) == bits(list[index + 1]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


print_list(subsequence_eleven(read_list()))

