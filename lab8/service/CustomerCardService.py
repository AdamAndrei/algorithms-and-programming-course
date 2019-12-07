import random
import string

from domain.CustomerCard import CustomerCard
from domain.CustomerCardValidator import CustomerCardValidator
from my_tools.my_sorted import my_sorted
from repository.GenericRepository import GenericRepository


class CustomerCardService:
    def __init__(self,
                 customer_card_repository: GenericRepository,
                 customer_card_validator: CustomerCardValidator,
                 transaction_repository: GenericRepository,
                 medicine_repository: GenericRepository):
        self.__customer_card_repository = customer_card_repository
        self.__customer_card_validator = customer_card_validator
        self.__transaction_repository = transaction_repository
        self.__medicine_repository = medicine_repository

    def add_customer_card(self,
                          customer_card_id,
                          customer_name,
                          customer_first_name,
                          customer_cnp,
                          birth_date,
                          registration_date,
                          is_removed):
        """
        Function creates a card
        :param is_removed:
        :param customer_card_id: int
        :param customer_name: string
        :param customer_first_name: string
        :param customer_cnp: int
        :param birth_date: string
        :param registration_date: string
        """
        customer_card = CustomerCard(customer_card_id,
                                     customer_name,
                                     customer_first_name,
                                     customer_cnp,
                                     birth_date,
                                     registration_date,
                                     is_removed)
        self.__customer_card_validator.validate_date(birth_date)
        self.__customer_card_validator.validate_date(registration_date)
        self.__customer_card_repository.ensure_unique_cnp(customer_card)
        self.__customer_card_validator.validate_customer_card(customer_card)
        self.__customer_card_repository.create(customer_card)

    def get_list_of_customer_cards_that_match(self, given_string):
        """
        Function finds all the cards that have the given string in them
        :param given_string: string
        :return: a list of CustomerCards objects that contain the string
        """
        found_customer_cards = []
        for customer_card in self.__customer_card_repository.read_all():
            if given_string in customer_card.get_text_format():
                found_customer_cards.append(customer_card)
        return found_customer_cards

    def get_all_cards(self):
        """
        Gets all cards from repository
        :return: a list of CustomerCard objects
        """
        found_cards = []
        for card in self.__customer_card_repository.read_all():
            found_cards.append(card)
        return found_cards

    def get_customer_cards_in_descending_order_by_discount(self):
        """

        :return: list of cards ordered by the discount received
        """
        list_of_customer_cards = self.__customer_card_repository.read_all()
        max_per_id = {}
        list_of_card_id = []
        for card in self.__customer_card_repository.read_all():
            list_of_card_id.append(card.get_id_entity())
        for transaction in self.__transaction_repository.read_all():
            if transaction.get_customer_card_transaction_id() in list_of_card_id:
                medicine = self.__medicine_repository.read_by_id(transaction.get_medicine_transacted_id())
                if medicine.get_recipe_need():
                    amount_of_discount = transaction.get_pieces_number() * ((15 * medicine.get_medicine_price()) / 100)
                    if transaction.get_customer_card_transaction_id() not in max_per_id:
                        max_per_id[transaction.get_customer_card_transaction_id()] = 0
                    max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
                else:
                    amount_of_discount = transaction.get_pieces_number() * ((10 * medicine.get_medicine_price()) / 100)
                    if transaction.get_customer_card_transaction_id() not in max_per_id:
                        max_per_id[transaction.get_customer_card_transaction_id()] = 0
                    max_per_id[transaction.get_customer_card_transaction_id()] += amount_of_discount
        # list_of_filtered_customer_cards = []
        # for card in list_of_customer_cards:
        #     if card.get_id_entity() in max_per_id:
        #         list_of_filtered_customer_cards.append(card)
        # for index in range(len(list_of_filtered_customer_cards) - 1):
        #     for k in range(index, len(list_of_filtered_customer_cards)):
        #         card_index = list_of_filtered_customer_cards[index]
        #         card_k = list_of_filtered_customer_cards[k]
        #         if max_per_id[card_index.get_id_entity()] < max_per_id[card_k.get_id_entity()]:
        #             list_of_filtered_customer_cards[index] = card_k
        #             list_of_filtered_customer_cards[k] = card_index
        list_of_filtered_customer_cards = list(filter(lambda customer_card: customer_card.get_id_entity() in max_per_id,
                                                      list_of_customer_cards))
        final_list = my_sorted(list_of_filtered_customer_cards,
                               key=lambda customer_card: max_per_id[customer_card.get_id_entity()], reverse=True)
        list_of_discounts_received = []
        for card in final_list:
            list_of_discounts_received.append(max_per_id[card.get_id_entity()])
        list_of_cards_and_discounts = zip(final_list, list_of_discounts_received)
        return list_of_cards_and_discounts

    def update_customer_card(self,
                             customer_card_id,
                             new_customer_name,
                             new_customer_first_name,
                             new_customer_cnp,
                             new_birth_date,
                             new_registration_date,
                             new_is_removed):
        customer_card = CustomerCard(customer_card_id,
                                     new_customer_name,
                                     new_customer_first_name,
                                     new_customer_cnp,
                                     new_birth_date,
                                     new_registration_date,
                                     new_is_removed)
        self.__customer_card_validator.validate_date(new_birth_date)
        self.__customer_card_validator.validate_date(new_registration_date)
        self.__customer_card_repository.ensure_unique_cnp(customer_card)
        self.__customer_card_validator.validate_customer_card(customer_card)
        self.__customer_card_repository.update(customer_card)

    def delete_customer_card_and_transactions(self, id_customer_card):
        customer_card = self.__customer_card_repository.read_by_id(id_customer_card)
        customer_name = customer_card.get_customer_name()
        customer_first_name = customer_card.get_customer_first_name()
        customer_cnp = customer_card.get_customer_cnp()
        birth_date = customer_card.get_birth_date()
        registration_date = customer_card.get_registration_date()
        self.update_customer_card(id_customer_card, customer_name, customer_first_name, customer_cnp, birth_date,
                                  registration_date, True)
        for transaction in self.__transaction_repository.read_all():
            if transaction.get_customer_card_transaction_id == id_customer_card:
                self.__transaction_repository.delete(transaction.get_id_entity())

    def populate_cards(self, n):
        list_of_id = []
        list_of_cnp = []
        for card in self.__customer_card_repository.read_all():
            card_id = card.get_id_entity()
            list_of_id.append(card_id)
            card_cnp = card.get_customer_cnp()
            list_of_cnp.append(card_cnp)
        sorted_list = sorted(list_of_id)
        start_id = sorted_list[-1] + 1
        cnp_sorted_list = sorted(list_of_cnp)
        start_cnp = cnp_sorted_list[-1] + 1
        letters = string.ascii_letters
        for i in range(n):
            customer_name = ''.join(random.choice(letters) for i in range(15))
            customer_first_name = ''.join(random.choice(letters) for i in range(15))
            cnp = int(random.randint(1000000000000, 9999999999999))
            if cnp not in list_of_cnp:
                good_cnp = cnp
            else:
                good_cnp = start_cnp
            day = int(random.randint(1, 31))
            month = int(random.randint(1, 12))
            year = int(random.randint(2000, 2019))
            birth_date = "{}/{}/{}".format(day, month, year)
            reg_day = int(random.randint(1, 31))
            reg_month = int(random.randint(1, 12))
            reg_year = int(random.randint(2000, 2019))
            registration_date = "{}/{}/{}".format(reg_day, reg_month, reg_year)
            is_removed = random.choice([True, False])
            customer_card = CustomerCard(start_id, customer_name, customer_first_name, good_cnp, birth_date,
                                         registration_date, is_removed)
            self.__customer_card_validator.validate_customer_card(customer_card)
            self.__customer_card_repository.create(customer_card)
            start_id += 1
        return self.__customer_card_repository.read_all()
