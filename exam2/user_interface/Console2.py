from exceptions.InvaidCircleIdException import InvalidCircleIdException
from exceptions.InvalidRadiusException import InvalidRadiusException
from service.CircleService import CircleService


class Console:
    def __init__(self, circle_service: CircleService):
        self.__circle_service = circle_service

    @staticmethod
    def __show_menu():
        print("1. Add circle")
        print("2. Get circles in descending order by area")
        print("3. Get circles that contain one point")
        print("4. Delete all circles that have the radius between two given values")
        print("5. Print all circles")
        print("6. Draw circles with minimum and maximum radius")
        print("Exit")

    def __handle_add(self):
        try:
            circle_id = int(input("Circle id: "))
            circle_abscissa = float(input("Center abscissa: "))
            circle_ordinate = float(input("Center ordinate: "))
            circle_radius = float(input("Circle radius: "))
            self.__circle_service.add_circle(circle_id, circle_abscissa, circle_ordinate, circle_radius)
            print("")
            print("Circle added!!!")
            print("")
        except ValueError as v:
            print(v)
        except InvalidCircleIdException as a:
            print(a)
        except InvalidRadiusException as s:
            print(s)

    def __handle_get_descending_order(self):
        circles_list = self.__circle_service.get_circles_in_descending_order_by_area()
        for circle in circles_list:
            print(circle)

    def __handle_get_circles_by_point(self):
        try:
            a = float(input("The abscissa for the point: "))
            b = float(input("The ordinate for the point: "))
            circles_list = self.__circle_service.get_all_circles_that_contain_one_point(a, b)
            for circle in circles_list:
                print(circle)
        except ValueError as d:
            print(d)

    def __handle_remove_circles_by_radius(self):
        try:
            a = float(input("Give the first number: "))
            b = float(input("Give the second number: "))
            self.__circle_service.remove_circles_with_some_radius(a, b)
        except ValueError as f:
            print(f)

    def __handle_print_circles(self):
        for circle in self.__circle_service.read_all():
            print(circle)

    def __handle_draw_circles(self):
        print(self.__circle_service.draw_the_circles())

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Option: ")
            if op == '1':
                self.__handle_add()
            elif op == '2':
                self.__handle_get_descending_order()
            elif op == '3':
                self.__handle_get_circles_by_point()
            elif op == '4':
                self.__handle_remove_circles_by_radius()
            elif op == '5':
                self.__handle_print_circles()
            elif op == '6':
                self.__handle_draw_circles()
            elif op == 'exit' or op == 'Exit':
                break
