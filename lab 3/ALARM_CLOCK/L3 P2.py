def is_prime(n):
    # descriere:verifica daca un numar este prim
    # in:un  numar natural n
    # out:True daca e prim,False daca nu e prim
    if n >= 2:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
        return True
    else:
        return False


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

def subsequence_two(list):
    beststart = 0
    bestcount = 0
    curentstart = 0
    curentcount = 0

    for index in range(len(list) - 1):
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



print_list(subsequence_two(read_list()))
