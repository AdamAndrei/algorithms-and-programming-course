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
        -verifica daca un numar intreg n este divizibil cu un numar intreg k
In:
        -numar natural n
Out:
        -True daca e divizibil ,False daca nu e divizibil
"""


def divide(n, k):
    if n % k == 0:
        return True
    else:
        return False


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere divizibile cu un numar intreg k
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere divizibile cu un numar intreg k 
"""


def subsequence_six(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0
    k = int(input("Numbers divide by:"))
    for index in range(len(list)):
        if divide(list[index], k):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


print_list(subsequence_six(read_list()))
