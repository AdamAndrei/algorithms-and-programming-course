import unittest

from domain.CustomerCardValidator import CustomerCardValidator
from repository.GenericRepository import GenericRepository
from service.CustomerCardService import CustomerCardService


class CustomerCardServiceTest(unittest.TestCase):
    def test_add_customer_card(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository("test.pickle")
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        customer_card_service = CustomerCardService(customer_card_repository, customer_card_validator,
                                                    transaction_repository, medicine_repository)
        customer_card_service.add_customer_card(1, "Adam", "Andrei", 5010306015562, "06/03/2001", "19/10/2018", False)
        self.assertEqual(len(customer_card_service.get_all_cards()), 1)
        customer_card_repository.delete(1)

    def test_update_customer_card(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository("test.pickle")
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        customer_card_service = CustomerCardService(customer_card_repository, customer_card_validator,
                                                    transaction_repository, medicine_repository)
        customer_card_service.add_customer_card(1, "Adam", "Andrei", 5020306015562, "06/03/2001", "19/10/2018", False)
        customer_card_service.update_customer_card(1, "Adams", "Andrei", 5010306015562, "06/03/2001",
                                                   "19/10/2018", False)
        card = customer_card_repository.read_by_id(1)
        self.assertEqual(card.get_customer_name(), "Adams")
        customer_card_repository.delete(1)

    def test_get_list_of_customer_cards_that_match(self):
        customer_card_validator = CustomerCardValidator()
        customer_card_repository = GenericRepository("test.pickle")
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        customer_card_service = CustomerCardService(customer_card_repository, customer_card_validator,
                                                    transaction_repository, medicine_repository)
        customer_card_service.add_customer_card(1, "Adam", "Andrei", 5010306015562, "06/03/2001", "19/10/2018", False)
        customer_card_service.add_customer_card(2, "Adams", "Andrei", 5020306015562, "06/03/2001", "19/10/2018", False)
        customer_card_service.add_customer_card(3, "Adams", "Andrei", 5030306015562, "06/03/2001", "19/10/2018", False)
        list_of_cards = customer_card_service.get_list_of_customer_cards_that_match("Adams")
        self.assertEqual(len(list_of_cards), 2)
        customer_card_repository.delete(1)
        customer_card_repository.delete(2)
        customer_card_repository.delete(3)
