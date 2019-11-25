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


def get_number_of_digit(n):
    nr = 0
    while n > 0:
        nr += 1
        n = n // 10
    return nr


def read_number():
    x = int(input("da un numar frate:   "))
    return x


def all_numbers(x):
    if is_prime(x):
        print(x, "ai dat un numar prim, Bravo!")
        for i in range(get_number_of_digit(x)):
            a = (x // (10 ** (i + 1))) * (10 ** i) + (x % 10 ** (i + 1)) % (10 ** i)
            if is_prime(a):
                print(a, 'ii prim frate ')
            else:
                print(a, 'nu ii prim frate ')
    else:
        print(x, "Ce facem aici? Asta nu ii prim, mai inceearca ")


def print_adam():
    print("    /\      |\        /\      |      |")
    print("   /  \     | \      /  \     |\    /|")
    print("  /____\    |  \    /____\    | \  / |")
    print(" /      \   |  /   /      \   |  \/  |")
    print("/        \  |_/   /        \  |      |")


print_adam()

all_numbers(read_number())

print_adam()

