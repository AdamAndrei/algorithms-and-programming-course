
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
        -returneaza numarul de divizori ai unui numar intreg
In:
        -un numar intreg n
Out:
        -numarul de divizori,un numar intreg
"""


def divisors_number(n):
    number_of_divisors = 0
    for d in range(1, n):
        if n % d == 0:
            number_of_divisors += 1
    return number_of_divisors


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu acelasi numar de divizori
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu acelasi numar de divizori
"""


def subsequence_twelve(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
        if divisors_number(list[index]) == divisors_number(list[index + 1]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


print_list(subsequence_twelve(read_list()))





