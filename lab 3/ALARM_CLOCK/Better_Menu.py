def test_subsequence():
    assert(subsequence_four(list[2, 4, 8, 16, 3, 5, 6, 7, 9, 10]) == (list[2, 4, 8, 16]))
    assert (subsequence_eleven(list[2, 4, 8, 16, 3, 5, 6, 7, 9, 10]) == (list[3, 5, 6, 7, 9, 10]))


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
    import math
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
        -returneaza o lista cu cea mai lunga subsecventa de numere prime
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere prime
"""


def subsequence_two(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list)):
        if is_prime(list[index]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere ordonate crescator
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere ordonate crescator
"""


def subsequence_four(list):
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
    return list[beststart: beststart + bestcount + 1]


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
    k = int(input("Divide number by:"))
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


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere neprime
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de  numere neprime
"""


def subsequence_seven(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list)):
        if not is_prime(list[index]):
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount]


"""
Description:
        -returneaza o lista cu cea mai lunga subsecventa de numere cu aceeasi paritate
In:
        -o lista de numere intregi
Out:
        -lista cu cea mai lunga subsecventa de numere cu aceeasi paritate
"""


def subsequence_ten(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
        if list[index] % 2 == list[index + 1] % 2:
            curentcount += 1
            if curentcount == 1:
                curentstart = index
            if curentcount > bestcount:
                bestcount = curentcount
                beststart = curentstart
        else:
            curentcount = 0
    return list[beststart: beststart + bestcount + 1]


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


def bits(number):
    a = two_base(number)
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


"""
Description:
        -stabileste daca toate ciferele unui numar sun
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


"""
Description:
        -creeaza un meniu
"""


def print_menu():
    print("1 - Citire date")
    print("2 - Determina cea mai lunga subsecventa de numere ordonate crescator:")
    print("3 - Determina cea mai lunga subsecventa de numere cu acelasi numar de biti de 1 in scrierea binara:")
    print("4 - Determina cea mai lunga subsecventa de numere prime:")
    print("5 - Determina cea mai lunga subsecventa de numere palindroame:")
    print("6 - Determina cea mai lunga subsecventa de numere divizibile cu un numar intreg k citit:")
    print("7 - Determina cea mai lunga subsecventa de numere neprime:")
    print("8 - Determina cea mai lunga subsecventa de numere cu aceeasi paritate")
    print("9 - Determina cea mai lunga subsecventa de numere cu acelasi numar de divizori:")
    print("10 - Determina cea mai lunga subsecventa de numere cu toate cifrele numere prime:")
    print("11 - Determina cea mai lunga subsecventa de numere patrate perfecte:")
    print("12 - Determina cea mai lunga subsecventade  numere cu numarul de cifre in ordine descrescatoare:")
    print("13 - Iesire")


"""
Description:
        -functia principala
"""


def main():
    print_menu()
    chosennumber = int(input("Numarul citit= "))
    list = []
    while chosennumber != 13:
        if chosennumber == 1:
            list = read_list()
        elif chosennumber == 2:
            print_list(subsequence_four(list))
        elif chosennumber == 3:
            print_list(subsequence_eleven(list))
        elif chosennumber == 4:
            print_list(subsequence_two(list))
        elif chosennumber == 5:
            print_list(subsequence_five(list))
        elif chosennumber == 6:
            print_list(subsequence_six(list))
        elif chosennumber == 7:
            print_list(subsequence_seven(list))
        elif chosennumber == 8:
            print_list(subsequence_ten(list))
        elif chosennumber == 9:
            print_list(subsequence_twelve(list))
        elif chosennumber == 10:
            print_list(subsequence_thirteen(list))
        elif chosennumber == 11:
            print_list(subsequence_one(list))
        elif chosennumber == 12:
            print_list(subsequence_eighteen(list))
        elif chosennumber == 13:
            break
        print_menu()
        chosennumber = int(input("Numarul este: "))


main()
