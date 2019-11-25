import unittest

from lab8.domain.Medicine import Medicine
from lab8.repository.MedicineRepository import MedicineRepository


class MedicineRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__medicine_repository = MedicineRepository("medicine_test.txt")

    def tearDown(self) -> None:
        for medicine in self.__medicine_repository.read_all():
            self.__medicine_repository.delete(medicine.get_medicine_id())

    def test_add_medicine_raise_exception_duplicated_id(self):
        medicine = Medicine(2, "paracetamol", "fares", 23, True)
        self.__medicine_repository.create(medicine)
        self.assertEqual(self.__medicine_repository.read_by_id(1), medicine)
