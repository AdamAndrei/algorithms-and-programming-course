import copy


def read_n():
    n = int(input("n ="))
    return n


def read_matrix(n):
    a = []
    for index in range(n):
        b = int(input("elment = "))
        a.append(b)
    return a


def max_product(list):
    list_two = []
    lista = copy.deepcopy(list)
    a = 0
    b = len(list)
    for i in range(b):
        lista.pop(i)
        p = lista
        for j in range(len(lista)):
            p.pop(j)
            q = p
            for k in range(len(q)):
                if abs(list[i] * list[j] * list[k]) > a:
                    a = list[i] * list[j] * list[k]
                    list_one = [list[i], list[j], list[k]]
                    list_two.append(list_one)
    return list_two[-1]


print(max_product(read_matrix(read_n())))
