import unittest

from domain.Medicine import Medicine


class MedicineTest(unittest.TestCase):
    def test_not_equal(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True, False)
        medicine_two = Medicine(2, 'adrenalin', 'fares', 23, True, False)
        self.assertNotEqual(unittest.TestCase, medicine_one, medicine_two)

    def test_equal(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True, False)
        medicine_two = Medicine(1, 'paracetamol', "fares", 23, True, False)
        self.assertEqual(medicine_one, medicine_two)

    def test_getter(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True, False)
        self.assertEqual(1, medicine_one.get_id_entity())
        self.assertEqual('paracetamol', medicine_one.get_medicine_name())
        self.assertEqual('fares', medicine_one.get_name_medicine_producer())
        self.assertEqual(23, medicine_one.get_medicine_price())
        self.assertEqual(True, medicine_one.get_recipe_need())

    def test_get_text_format(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True, False)
        medicine_string = medicine_one.get_text_format()
        self.assertEqual(medicine_string, "1,paracetamol,fares,23,True")

