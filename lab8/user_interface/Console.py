from exception.InvalidCNPException import InvalidCNPException
from exception.InvalidCustomerCardException import InvalidCustomerCardException
from exception.InvalidIdException import InvalidIdException
from exception.InvalidMedicineException import InvalidMedicineException
from exception.InvalidTransactionException import InvalidTransactionException
from service.CustomerCardService import CustomerCardService
from service.MedicineService import MedicineService
from service.TransactionService import TransactionService


class Console:
    def __init__(self,
                 medicine_service: MedicineService,
                 customer_card_service: CustomerCardService,
                 transaction_service: TransactionService):
        self.__medicine_service = medicine_service
        self.__customer_card_service = customer_card_service
        self.__transaction_service = transaction_service

    @staticmethod
    def __show_menu():
        print("")
        print("Choose your option:")
        print("")
        print("1. Add medicine")
        print("2. Search medicine by string")
        print("3. Print all drugs")
        print("4. Add card")
        print("5. Search customer card by string")
        print("6. Print all cards")
        print("7. Add transaction")
        print("8. Populate medicine")
        print("9. Print all transactions")
        print("10. Print all medicines in order by number of pieces sold")
        print("11. Print all customer cards in order by amount of discount received")
        print("12. Expense medicines")
        print("13. Display all the transactions made between two given dates ")
        print("14. Remove all the transactions made between two given dates ")
        print("15. Remove drug by id ")
        print("16. Remove card by id ")
        print("17. Update medicine ")
        print("18. Update customer card ")
        print("19. Update transaction ")
        print("20. Populate customer cards ")
        print("21. Populate transactions ")
        print("Exit")
        print("")

    def __add_medicine(self):
        try:
            medicine_id = int(input("medicine id ="))
            medicine_name = input("medicine name = ")
            medicine_producer_name = input("medicine_producer_name")
            medicine_price = float(input("medicine price ="))
            medicine_recipe_need = input("recipe need = ")
            if medicine_recipe_need == 'True' or medicine_recipe_need == 'true':
                good_medicine_recipe_need = True
            else:
                good_medicine_recipe_need = False
            self.__medicine_service.add_medicine(medicine_id, medicine_name, medicine_producer_name, medicine_price,
                                                 good_medicine_recipe_need, False)
            print("")
            print("Medicine added!")
        except InvalidMedicineException as a:
            print(a)
        except InvalidIdException as p:
            print(p)
        except ValueError as t:
            print(t)

    def __add_customer_card(self):
        try:
            customer_card_id = int(input("customer card id = "))
            customer_name = input("customer name = ")
            customer_first_name = input("customer_first_name  = ")
            customer_cnp = int(input("customer cnp = "))
            print("For date please use 'day/month/year' format!!!")
            birth_date = input("birth date = ")
            registration_date = input("registration date = ")
            self.__customer_card_service.add_customer_card(customer_card_id, customer_name, customer_first_name,
                                                           customer_cnp, birth_date, registration_date, False)
            print("")
            print("Card added!")
        except InvalidCustomerCardException as v:
            print(v)
        except InvalidCNPException as a:
            print(a)
        except InvalidIdException as d:
            print(d)
        except ValueError as o:
            print(o)

    def __add_transaction(self):
        try:
            transaction_id = int(input("transaction id = "))
            medicine_transacted_id = int(input("medicine transacted id = "))
            intermediate_customer_card_transacted_id = input("customer card transacted id =")
            if intermediate_customer_card_transacted_id != '':
                customer_card_transacted_id = int(intermediate_customer_card_transacted_id)
            else:
                customer_card_transacted_id = intermediate_customer_card_transacted_id
            pieces_number = int(input("pieces number = "))
            print("For date please use 'day/month/year' format!!!")
            date = input("date = ")
            time = float(input("time ="))
            self.__transaction_service.add_transaction(transaction_id,
                                                       medicine_transacted_id,
                                                       customer_card_transacted_id,
                                                       pieces_number,
                                                       date,
                                                       time)
            result = self.__transaction_service.get_discount(medicine_transacted_id, customer_card_transacted_id,
                                                             pieces_number)
            print(self.__transaction_service.get_discount(medicine_transacted_id, customer_card_transacted_id,
                                                          pieces_number))
            if result == [] and customer_card_transacted_id != '':
                print("This customer doesn't have card!")
                print("Do you want to create a card for this customer?")
                x = input("Your answer: ")
                if x == "Yes" or x == "yes":
                    print("Then give his data: ")
                    customer_name = input("Customer name: ")
                    customer_first_name = input("Customer first name: ")
                    customer_cnp = int(input("Customer CNP: "))
                    birth_date = input("Customer birth date = ")
                    registration_date = input("Customer registration date = ")
                    self.__customer_card_service.add_customer_card(customer_card_transacted_id,
                                                                   customer_name,
                                                                   customer_first_name,
                                                                   customer_cnp,
                                                                   birth_date,
                                                                   registration_date,
                                                                   False)
                    print("")
                    print("Card added!")
                else:
                    print("")
                    print("Understood!")
            print("")
            print("Transaction added!")
        except InvalidCustomerCardException as s:
            print(s)
        except InvalidIdException as f:
            print(f)
        except ValueError as y:
            print(y)
        except InvalidMedicineException as a:
            print(a)
        except InvalidCNPException as a:
            print(a)

    def __search_medicine(self):
        string = input("Give a text: ")
        result = self.__medicine_service.get_list_of_drugs_that_match(string)
        for medicine in result:
            print(medicine)

    def __search_customer_card(self):
        string = input("Give a text ")
        result = self.__customer_card_service.get_list_of_customer_cards_that_match(string)
        for customer_card in result:
            print(customer_card)

    def __handle_show_medicine(self):
        result = self.__medicine_service.get_all_drugs()
        for drug in result:
            print(drug)

    def __handle_show_transactions(self):
        result = self.__transaction_service.get_all_transactions()
        for transaction in result:
            print(transaction)

    def __handle_show_cards(self):
        result = self.__customer_card_service.get_all_cards()
        for card in result:
            print(card)

    def __handle_populate(self):
        try:
            x = int(input("Give number = "))
            result = self.__medicine_service.populate(x)
            for drug in result:
                print(drug)
        except ValueError as a:
            print(a)

    def __handle_order_medicine(self):
        result = self.__medicine_service.get_medicines_id_in_descending_order_by_pieces_number()
        for drug in result:
            print(drug[0], "Number of pieces sold:", drug[1])

    def __handle_oder_customer_cards(self):
        result = self.__customer_card_service.get_customer_cards_in_descending_order_by_discount()
        for card in result:
            print(card[0], "Discount received:", card[1])

    def __handle_expense_medicine(self):
        try:
            percentage = float(input("Give percentage: "))
            maximum_price = float(input("Give the price from which you want to expensive: "))
            self.__medicine_service.expensive_medicine(percentage, maximum_price)
            print("Expensive made")
        except ValueError as g:
            print(g)

    def __handle_transactions_between_two_dates(self):
        print("Enter the data between which you want the transactions to be displayed:")
        try:
            date_one = input("First date: ")
            date_two = input("Second date: ")
            result = self.__transaction_service.get_transactions_between_two_dates(date_one, date_two)
            print(result)
            if len(result) != 0:
                for i in range(len(result)):
                    print(self.__transaction_service.get_transaction(result[i]))
            else:
                print(result)
        except InvalidTransactionException as r:
            print(r)
        except ValueError as w:
            print(w)

    def __handle_remove_transactions_between_dates(self):
        try:
            print("Enter the data between which you want the transactions to be removed:")
            date_one = input("First date: ")
            date_two = input("Second date: ")
            self.__transaction_service.remove_transactions_between_two_dates(date_one, date_two)
            result = self.__transaction_service.get_all_transactions()
            for transaction in result:
                print(transaction)
        except InvalidTransactionException as p:
            print(p)
        except ValueError as h:
            print(h)

    def __handle_remove_drugs(self):
        x = int(input("Give the id by which you want to delete: "))
        self.__medicine_service.delete_medicine_and_transactions(x)
        result = self.__medicine_service.get_all_drugs()
        for drug in result:
            print(drug)

    def __handle_remove_cards(self):
        x = int(input("Give the id by which you want to delete: "))
        self.__customer_card_service.delete_customer_card_and_transactions(x)
        result = self.__customer_card_service.get_all_cards()
        for card in result:
            print(card)

    def __handle_update_medicine(self):
        try:
            medicine_id = int(input("medicine id ="))
            medicine_name = input("medicine name = ")
            medicine_producer_name = input("medicine_producer_name = ")
            medicine_price = float(input("medicine price = "))
            medicine_recipe_need = input("recipe need = ")
            if medicine_recipe_need == 'True' or medicine_recipe_need == 'true':
                good_medicine_recipe_need = True
            else:
                good_medicine_recipe_need = False
            self.__medicine_service.update_medicine(medicine_id, medicine_name, medicine_producer_name, medicine_price,
                                                    good_medicine_recipe_need, False)
            print("")
            print("Medicine updated!")
        except InvalidMedicineException as a:
            print(a)
        except InvalidIdException as p:
            print(p)
        except ValueError as t:
            print(t)

    def __handle_update_customer_card(self):
        try:
            customer_card_id = int(input("customer card id = "))
            customer_name = input("customer name = ")
            customer_first_name = input("customer_first_name  = ")
            customer_cnp = int(input("customer cnp = "))
            print("For date please use 'day/month/year' format!!!")
            birth_date = input("birth date = ")
            registration_date = input("registration date = ")
            self.__customer_card_service.update_customer_card(customer_card_id, customer_name, customer_first_name,
                                                              customer_cnp, birth_date, registration_date, False)
            print("")
            print("Card updated!")
        except InvalidCustomerCardException as v:
            print(v)
        except InvalidCNPException as a:
            print(a)
        except InvalidIdException as d:
            print(d)
        except ValueError as o:
            print(o)

    def __handle_update_transaction(self):
        try:
            transaction_id = int(input("transaction id = "))
            medicine_transacted_id = int(input("medicine transacted id = "))
            intermediate_customer_card_transacted_id = input("customer card transacted id =")
            if intermediate_customer_card_transacted_id != '':
                customer_card_transacted_id = int(intermediate_customer_card_transacted_id)
            else:
                customer_card_transacted_id = intermediate_customer_card_transacted_id
            pieces_number = int(input("pieces number = "))
            print("For date please use 'day/month/year' format!!!")
            date = input("date = ")
            time = float(input("time ="))
            self.__transaction_service.update_transaction(transaction_id,
                                                          medicine_transacted_id,
                                                          customer_card_transacted_id,
                                                          pieces_number,
                                                          date,
                                                          time)
            result = self.__transaction_service.get_discount(medicine_transacted_id, customer_card_transacted_id,
                                                             pieces_number)
            print(self.__transaction_service.get_discount(medicine_transacted_id, customer_card_transacted_id,
                                                          pieces_number))
            if result == [] and customer_card_transacted_id != '':
                print("This customer doesn't have card!")
                print("Do you want to create a card for this customer?")
                x = input("Your answer: ")
                if x == "Yes" or x == "yes":
                    print("Then give his data: ")
                    customer_name = input("Customer name: ")
                    customer_first_name = input("Customer first name: ")
                    customer_cnp = int(input("Customer CNP: "))
                    birth_date = input("Customer birth date = ")
                    registration_date = input("Customer registration date = ")
                    self.__customer_card_service.add_customer_card(customer_card_transacted_id,
                                                                   customer_name,
                                                                   customer_first_name,
                                                                   customer_cnp,
                                                                   birth_date,
                                                                   registration_date,
                                                                   False)
                    print("")
                    print("Card added!")
                else:
                    print("")
                    print("Understood!")
            print("")
            print("Transaction updated!")
        except InvalidCustomerCardException as s:
            print(s)
        except InvalidIdException as f:
            print(f)
        except ValueError as y:
            print(y)
        except InvalidMedicineException as a:
            print(a)
        except InvalidCNPException as a:
            print(a)

    def __handle_populate_customer_card(self):
        try:
            n = int(input("Give the number: "))
            for card in self.__customer_card_service.populate_cards(n):
                print(card)
        except ValueError as d:
            print(d)

    def __handle_populate_transactions(self):
        try:
            n = int(input("Give the number: "))
            for transaction in self.__transaction_service.populate_transactions(n):
                print(transaction)
        except ValueError as w:
            print(w)

    def run_console(self):
        while True:
            self.__show_menu()
            op = input('Option: ')
            if op == '1':
                self.__add_medicine()
            elif op == '2':
                self.__search_medicine()
            elif op == '3':
                self.__handle_show_medicine()
            elif op == '4':
                self.__add_customer_card()
            elif op == '5':
                self.__search_customer_card()
            elif op == '6':
                self.__handle_show_cards()
            elif op == '7':
                self.__add_transaction()
            elif op == '8':
                self.__handle_populate()
            elif op == '9':
                self.__handle_show_transactions()
            elif op == '10':
                self.__handle_order_medicine()
            elif op == '11':
                self.__handle_oder_customer_cards()
            elif op == '12':
                self.__handle_expense_medicine()
            elif op == '13':
                self.__handle_transactions_between_two_dates()
            elif op == '14':
                self.__handle_remove_transactions_between_dates()
            elif op == '15':
                self.__handle_remove_drugs()
            elif op == '16':
                self.__handle_remove_cards()
            elif op == '17':
                self.__handle_update_medicine()
            elif op == '18':
                self.__handle_update_customer_card()
            elif op == '19':
                self.__handle_update_transaction()
            elif op == "20":
                self.__handle_populate_customer_card()
            elif op == "21":
                self.__handle_populate_transactions()
            elif op == 'Exit' or op == 'exit':
                break
