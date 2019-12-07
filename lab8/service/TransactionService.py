import datetime
import random

from domain.Transaction import Transaction
from domain.TransactionValidator import TransactionValidator
from exception.InvalidIdException import InvalidIdException
from repository.GenericRepository import GenericRepository


class TransactionService:
    def __init__(self,
                 transaction_repository: GenericRepository,
                 transaction_validator: TransactionValidator,
                 customer_card_repository: GenericRepository,
                 medicine_repository: GenericRepository):
        self.__transaction_repository = transaction_repository
        self.__transaction_validator = transaction_validator
        self.__customer_card_repository = customer_card_repository
        self.__medicine_repository = medicine_repository

    def add_transaction(self,
                        transaction_id,
                        medicine_transacted_id,
                        customer_card_transaction_id,
                        pieces_number,
                        date,
                        time):
        """
        Creates a transaction
        :param transaction_id: int
        :param medicine_transacted_id: int
        :param customer_card_transaction_id: int
        :param pieces_number: int
        :param date: string
        :param time: string
        """
        if medicine_transacted_id not in self.get_medicines_id():
            raise InvalidIdException("There is no such medicine with that id")
        transaction = Transaction(transaction_id,
                                  medicine_transacted_id,
                                  customer_card_transaction_id,
                                  pieces_number,
                                  date,
                                  time)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.create(transaction)

    def get_all_transactions(self):
        """

        :return: all the transactions from storage
        """
        found_transactions = []
        for transaction in self.__transaction_repository.read_all():
            found_transactions.append(transaction)
        return found_transactions

    def get_transaction(self, transaction_id):
        """

        :param transaction_id: int
        :return: the Transaction object that has the given id
        """
        return self.__transaction_repository.read_by_id(transaction_id)

    def update_transaction(self,
                           new_transaction_id,
                           new_medicine_transacted_id,
                           new_customer_card_transaction_id,
                           new_pieces_number,
                           new_date,
                           new_time):
        """
        Update an object of Transaction type
        :param new_transaction_id: int
        :param new_medicine_transacted_id: int
        :param new_customer_card_transaction_id: int
        :param new_pieces_number: int
        :param new_date: string
        :param new_time: string
        """
        transaction = Transaction(new_transaction_id,
                                  new_medicine_transacted_id,
                                  new_customer_card_transaction_id,
                                  new_pieces_number,
                                  new_date,
                                  new_time)
        self.__transaction_validator.validate_transaction(transaction)
        self.__transaction_repository.update(transaction)

    def remove_transaction(self, transaction_id):
        """
        Deletes the Transaction object with the given id
        :param transaction_id: int
        """
        self.__transaction_repository.delete(transaction_id)

    def get_discount(self, medicine_transacted_id, customer_card_transacted_id, pieces_number):
        """
        Get discount for customers that have already a card
        :param medicine_transacted_id: int
        :param customer_card_transacted_id: int
        :param pieces_number: int
        :return: list with the discount and the price paid
        """
        medicine_price = self.__medicine_repository.read_by_id(medicine_transacted_id).get_medicine_price()
        medicine_recipe = self.__medicine_repository.read_by_id(medicine_transacted_id).get_recipe_need()
        customer_card_id = customer_card_transacted_id
        customers_card_id = []
        found_discount = []
        for customer_card in self.__customer_card_repository.read_all():
            found_id = customer_card.get_id_entity()
            customers_card_id.append(found_id)
        for i in range(len(customers_card_id)):
            if customer_card_id == int(customers_card_id[i]):
                if medicine_recipe:
                    found_discount.append("15% discount")
                    medicine_price_one = medicine_price - (medicine_price * (15 / 100))
                    the_amount_paid = medicine_price_one * pieces_number
                    found_discount.append(the_amount_paid)
                else:
                    found_discount.append("10% discount")
                    medicine_price_one = medicine_price - (medicine_price * (10 / 100))
                    the_amount_paid = medicine_price_one * pieces_number
                    found_discount.append(the_amount_paid)
        return found_discount

    @staticmethod
    def __get_date_in_format(date):
        """
        Transforms a string that represents a date into datetime format
        :param date: string
        :return: a datetime date
        """
        date_list = date.split(sep="/")
        year = int(date_list[2])
        month = int(date_list[1])
        day = int(date_list[0])
        date_in_date_format = datetime.datetime(year, month, day)
        return date_in_date_format

    def get_transactions_between_two_dates(self, date_one, date_two):
        """
        Gets all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        :return: list of Transaction objects type
        """
        list_of_transactions = []
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transactions.append(transaction.get_id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transactions.append(transaction.get_id_entity())
            elif difference == zero_days:
                list_of_transactions = []
        return list_of_transactions

    def remove_transactions_between_two_dates(self, date_one, date_two):
        """
        Deletes all the transactions made between two given dates
        :param date_one: string
        :param date_two: string
        """
        self.__transaction_validator.validate_date(date_one)
        self.__transaction_validator.validate_date(date_two)
        date_one_obj = self.__get_date_in_format(date_one)
        date_two_obj = self.__get_date_in_format(date_two)
        difference = date_two_obj - date_one_obj
        list_of_transaction_to_remove = []
        for transaction in self.__transaction_repository.read_all():
            checked_date = self.__get_date_in_format(transaction.get_date())
            zero_days = datetime.timedelta(0)
            if difference > zero_days:
                if (checked_date - date_one_obj) > zero_days and \
                        (date_two_obj - checked_date) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_id_entity())
            elif difference < zero_days:
                if (date_one_obj - checked_date) > zero_days and \
                        (checked_date - date_two_obj) > zero_days:
                    list_of_transaction_to_remove.append(transaction.get_id_entity())
            elif difference == zero_days:
                list_of_transaction_to_remove.append(transaction.get_id_entity())
        for i in range(len(list_of_transaction_to_remove)):
            self.remove_transaction(list_of_transaction_to_remove[i])

    def get_medicines_id(self):
        found_id = []
        for medicine in self.__medicine_repository.read_all():
            found_id.append(medicine.get_id_entity())
        return found_id

    def populate_transactions(self, n):
        list_of_transactions_id = []
        list_of_medicine_id = []
        list_of_customer_id = []
        for transaction in self.__transaction_repository.read_all():
            list_of_transactions_id.append(transaction.get_id_entity())
        for medicine in self.__medicine_repository.read_all():
            list_of_medicine_id.append(medicine.get_id_entity())
        for card in self.__customer_card_repository.read_all():
            list_of_customer_id.append(card.get_id_entity())
        sorted_list = sorted(list_of_transactions_id)
        start_id = sorted_list[-1] + 1
        for i in range(n):
            medicine_transacted_id = random.choice(list_of_medicine_id)
            customer_card_transacted_id = random.choice(list_of_customer_id)
            pieces_number = random.randint(1, 1000)
            day = int(random.randint(1, 31))
            month = int(random.randint(1, 12))
            year = int(random.randint(2000, 2019))
            date = "{}/{}/{}".format(day, month, year)
            time = float(random.randint(1, 24))
            transaction = Transaction(start_id, medicine_transacted_id, customer_card_transacted_id, pieces_number,
                                      date, time)
            self.__transaction_validator.validate_transaction(transaction)
            self.__transaction_repository.create(transaction)
            start_id += 1
        return self.__transaction_repository.read_all()
