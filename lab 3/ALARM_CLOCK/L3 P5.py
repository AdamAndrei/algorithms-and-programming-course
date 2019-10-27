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
        -verifica daca un numar este palindrom
In:
        -numar natural n
Out:
        -True daca e palindrom,False daca nu e palindrom
"""


def is_palindrome(x):
    ogl = 0
    n = x
    while n > 0:
        ld = n % 10
        ogl = ogl * 10 + ld
        n = n // 10
    if x == ogl:
        return True
    else:
        return False



"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere palindroame
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere palindroame
"""


def subsequence_five(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0
    for index in range(len(list)):
        if is_palindrome(list[index]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


print_list(subsequence_five(read_list()))
