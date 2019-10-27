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


def subsequence_sixteen(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 3):
        if (list[index + 1] - list[index]) ==:
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


print_list(subsequence_sixteen(read_list()))