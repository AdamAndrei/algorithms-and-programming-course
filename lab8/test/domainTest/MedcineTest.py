import unittest

from lab8.domain.Medicine import Medicine


class MedicineTest(unittest.TestCase):
    def test_not_equal(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True)
        medicine_two = Medicine(2, 'adrenalin', 'fares', 23, True)
        self.assertNotEqual(unittest.TestCase, medicine_one, medicine_two)

    def test_equal(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True)
        medicine_two = Medicine(1, 'paracetamol', "fares", 23, True)
        self.assertEqual(medicine_one, medicine_two)

    def test_getter(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True)
        self.assertEqual(1, medicine_one.get_medicine_id())
        self.assertEqual('paracetamol', medicine_one.get_medicine_name())
        self.assertEqual('fares', medicine_one.get_name_medicine_producer())
        self.assertEqual(23, medicine_one.get_medicine_price())
        self.assertEqual(True, medicine_one.get_recipe_need())

    def test_setter(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True)
        medicine_two = Medicine(1, 'adrenaline', "pharmacies", 24, False)
        medicine_one.set_medicine_name('adrenaline')
        medicine_one.set_name_medicine_producer('pharmacies')
        medicine_one.set_medicine_price(24)
        medicine_one.set_recipe_need(False)
        self.assertEqual(medicine_one.get_medicine_name(), 'adrenaline')
        self.assertEqual(medicine_one.get_name_medicine_producer(), "pharmacies")
        self.assertEqual(medicine_one.get_medicine_price(), 24)
        self.assertEqual(medicine_one.get_recipe_need(), False)
        self.assertEqual(medicine_one, medicine_two)

    def test_get_text_format(self):
        medicine_one = Medicine(1, 'paracetamol', "fares", 23, True)
        medicine_string = medicine_one.get_text_format()
        self.assertEqual(medicine_string, "1,paracetamol,fares,23,True")

