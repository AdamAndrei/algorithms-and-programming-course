def read_number_of_viruses():
    n = int(input("n = "))
    return n


def read_number_of_critical():
    k = int(input("k = "))
    return k

def virus(n, k):
    number_hours = 0
    while n >= k:
        if n % 2  == 0:
            number_hours += 1
            n = n / 2
        else:
            number_hours += 1
            n += 1
    return number_hours


print(virus(read_number_of_viruses(), read_number_of_critical()))

