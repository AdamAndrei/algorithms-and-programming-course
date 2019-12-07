

class Console:
    def __init__(self):
        pass

    @staticmethod
    def __show_menu():
        print("1.")
        print("2.")
        print("3.")
        print("4.")
        print("5.")
        print("6.")
        print("Exit")

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Option: ")
            if op == '1':
                pass
            elif op == '2':
                pass
            elif op == '3':
                pass
            elif op == '4':
                pass
            elif op == '5':
                pass
            elif op == '6':
                pass
            elif op == 'exit' or op == 'Exit':
                break
