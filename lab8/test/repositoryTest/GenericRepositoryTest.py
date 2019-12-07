import unittest

from domain.Medicine import Medicine
from repository.GenericRepository import GenericRepository


class GenericRepositoryTest(unittest.TestCase):
    def test_create(self):
        filename = "test.pickle"
        generic_repository = GenericRepository(filename)
        medicine = Medicine(1, "para", "fares", 12.1, True, False)
        generic_repository.create(medicine)
        storage = generic_repository.read_all()
        self.assertEqual(len(storage), 1)
        generic_repository.delete(1)

    def test_update(self):
        filename = "test.pickle"
        generic_repository = GenericRepository(filename)
        medicine = Medicine(1, "para", "fares", 12.1, True, False)
        generic_repository.create(medicine)
        medicine_to_update = Medicine(1, "para", "fares", 12.12, True, False)
        generic_repository.update(medicine_to_update)
        new_medicine = generic_repository.read_by_id(1)
        self.assertEqual(new_medicine.get_medicine_price(), 12.12)
        generic_repository.delete(1)
