import unittest

from domain.MedicineValidator import MedicineValidator
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from service.MedicineService import MedicineService
from service.TransactionService import TransactionService


class TransactionServiceTest(unittest.TestCase):
    def test_add_transaction(self):
        medicine_repository = GenericRepository("test.pickle")
        customer_card_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        transaction_validator = TransactionValidator()
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository, medicine_repository)
        medicine_service.add_medicine(2, "para", "fares", 12.12, True, False)
        transaction_service.add_transaction(1, 2, 3, 12, "12/11/2018", 12.23)
        medicine_repository.delete(2)
        self.assertEqual(len(transaction_service.get_all_transactions()), 1)
        transaction_repository.delete(1)

    def test_update_transaction(self):
        medicine_repository = GenericRepository("test.pickle")
        customer_card_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        transaction_validator = TransactionValidator()
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository, medicine_repository)
        medicine_service.add_medicine(2, "para", "fares", 12.12, True, False)
        transaction_service.add_transaction(1, 2, 3, 12, "12/11/2018", 12.23)
        transaction_service.update_transaction(1, 2, 4, 12, "12/11/2018", 12.23)
        medicine_repository.delete(2)
        transaction = transaction_repository.read_by_id(1)
        self.assertEqual(transaction.get_customer_card_transaction_id(), 4)
        transaction_repository.delete(1)

    def test_get_transactions_between_two_dates(self):
        medicine_repository = GenericRepository("test.pickle")
        customer_card_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test.pickle")
        transaction_validator = TransactionValidator()
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        transaction_service = TransactionService(transaction_repository, transaction_validator,
                                                 customer_card_repository, medicine_repository)
        medicine_service.add_medicine(2, "para", "fares", 12.12, True, False)
        medicine_service.add_medicine(5, "para", "fares", 12.12, True, False)
        medicine_service.add_medicine(6, "para", "fares", 12.12, True, False)
        transaction_service.add_transaction(1, 2, 3, 12, "12/11/2018", 12.23)
        transaction_service.add_transaction(3, 5, 3, 12, "13/11/2018", 12.23)
        transaction_service.add_transaction(4, 6, 3, 12, "15/11/2018", 12.23)
        medicine_repository.delete(2)
        medicine_repository.delete(5)
        medicine_repository.delete(6)
        list_of_transactions = transaction_service.get_transactions_between_two_dates("11/11/2018", "14/11/2018")
        self.assertEqual(len(list_of_transactions), 2)
        transaction_repository.delete(1)
        transaction_repository.delete(3)
        transaction_repository.delete(4)
