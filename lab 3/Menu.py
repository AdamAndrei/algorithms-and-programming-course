def test_subsequence():
    assert(subsequence_one(list[2, 4, 8, 16, 3, 5, 6, 7, 9, 10]) == (list[2, 4, 8, 16]))
    assert (subsequence_two(list[2, 4, 8, 16, 3, 5, 6, 7, 9, 10]) == (list[3, 5, 6, 7, 9, 10]))


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
        -returneaza o lista cu cea mai lunga subsecventa de numere ordonate crescator
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere ordonate crescator
"""


def subsequence_one(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
        if list[index] < list[index + 1]:
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return [beststart, beststart + bestcount]


"""
Description:
        -transforma un numar din baza 10 in baza 2
In:
        -un numar intreg 
Out:
        -un numar in baza 2
"""


def two_base(a):
    m = 0
    p = 1
    while a > 0:
        r = a % 2
        m = m + (r * p)
        p = p * 10
        a = a // 2
    return m


"""
Description:
        -numara de cate ori apar biti de 1 in scrierea in baza 2
In:
        -un numar in baza 2
Out:
        -un numar intreg
"""


def bits(Number):
    a = two_base(Number)
    number_of_one = 0
    while a > 0:
        ld = a % 10
        if ld == 1:
            number_of_one += 1
        a = a // 10
    return number_of_one


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scriere binara
"""


def subsequence_two(list):
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
    return [beststart, beststart + bestcount]


"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date")
    print("2 - Determina cea mai lunga subsecventa de numere ordonate crescator:")
    print("3 - Determina cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scrierea binara:")
    print("4 - Iesire")


"""
Description:
        -functia principala
"""


def main():
    print_menu()
    chosennumber = int(input("Numarul citit= "))
    list = []
    while chosennumber != 4:
        if chosennumber == 1:
            list = read_list()
        elif chosennumber == 2:
            print_list(subsequence_one(list))
        elif chosennumber == 3:
            print_list(subsequence_two(list))
        elif chosennumber == 4:
            break
        print_menu()
        chosennumber = int(input("Numarul este: "))




main()
