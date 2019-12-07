import unittest

from domain.MedicineValidator import MedicineValidator
from repository.GenericRepository import GenericRepository
from service.MedicineService import MedicineService


class MedicineServiceTest(unittest.TestCase):
    def test_add_medicine(self):
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test1.pickle")
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        medicine_service.add_medicine(1, "para", "fares", 12.0, True, False)
        self.assertEqual(len(medicine_repository.read_all()), 1)
        self.assertEqual(len(medicine_service.get_all_drugs()), 1)
        medicine_repository.delete(1)

    def test_update_medicine(self):
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test1.pickle")
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        medicine_service.add_medicine(1, "para", "fares", 12.0, True, False)
        medicine_service.update_medicine(1, "alg", "fares", 12.34, False, False)
        medicine = medicine_service.get_drug(1)
        self.assertEqual(medicine.get_medicine_name(), "alg")
        self.assertEqual(medicine.get_recipe_need(), False)
        medicine_repository.delete(1)

    def test_get_all_drugs_that_match(self):
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test1.pickle")
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        medicine_service.add_medicine(1, "para", "fares", 12.0, True, False)
        medicine_service.add_medicine(2, "alg", "fares", 12.0, True, False)
        medicine_service.add_medicine(3, "alga", "fares", 12.0, True, False)
        list_of_drugs = medicine_service.get_list_of_drugs_that_match("alg")
        self.assertEqual(len(list_of_drugs), 2)
        medicine_repository.delete(1)
        medicine_repository.delete(2)
        medicine_repository.delete(3)

    def test_populate(self):
        medicine_repository = GenericRepository("test.pickle")
        transaction_repository = GenericRepository("test1.pickle")
        medicine_validator = MedicineValidator()
        medicine_service = MedicineService(medicine_repository, medicine_validator, transaction_repository)
        medicine_service.add_medicine(1, "para", "fares", 12.0, True, False)
        medicine_service.populate(2)
        self.assertEqual(len(medicine_service.get_all_drugs()), 3)
        medicine_repository.delete(1)
        medicine_repository.delete(2)
        medicine_repository.delete(3)
