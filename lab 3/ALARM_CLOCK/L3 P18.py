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
        -numara cifrele unui numar intreg
In:
        -un numar intreg
Out:
        -numarul de cifre a numuarului 
"""


def number_of_digits(n):
    digits_number = 0
    while n > 0:
        digits_number += 1
        n = n // 10
    return digits_number


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere  cu numarul de cifre in ordine descrescatoare
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere cu numarul de cifre in ordine descrescatoare
"""


def subsequence_eighteen(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
        if number_of_digits(list[index]) > number_of_digits(list[index + 1]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


print_list(subsequence_eighteen(read_list()))