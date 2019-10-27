import math
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
        -stabileste daca un numar este patrat perfect
In:
        -un numar intreg
Out:
        -True daca e patrat perfect, False daca nu e patrat perfect
"""


def perfect_square(n):
    if int(math.sqrt(n)) == math.sqrt(n):
        return True
    else:
        return False


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere patrate perfecte
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere patrate perfecte
"""


def subsequence_one(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list)):
        if perfect_square(list[index]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


print_list(subsequence_one(read_list()))
