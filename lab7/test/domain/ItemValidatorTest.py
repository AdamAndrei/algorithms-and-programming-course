from lab7.domain.Item import Item
from lab7.exeption.InvalidItemException import InvalidItemException
from lab7.domain.ItemValidator import ItemValidator
import unittest

from lab7.repository.ItemRepository import ItemRepository


class ItemValidatorTest(unittest.TestCase):
    def test_validate_id_raises_exception(self):
        item = Item("a", "chair", "made", 23, "home")
        validator = ItemValidator(ItemRepository())
        self.assertRaises(InvalidItemException, lambda: validator.validate(item))

    def test_validate_price_raises_exception(self):
        item_one = Item(1, "chair", "made of wood", "c", "room")
        validator = ItemValidator(ItemRepository())
        self.assertRaises(InvalidItemException, lambda: validator.validate(item_one))

    def test_validate_description_not_null(self):
        item = Item(1, "chair", "", 23, "home")
        validator = ItemValidator(ItemRepository())
        self.assertRaises(InvalidItemException, lambda: validator.validate(item))

    def test_validate_name_not_null(self):
        item = Item(1, "", "made", 23, "home")
        validator = ItemValidator(ItemRepository())
        self.assertRaises(InvalidItemException, lambda: validator.validate(item))

    # def test_validate_unique_id(self):
    #     item = Item(1, "chair", "made", 23, "home")
    #     repository = ItemRepository()
    #     repository.add(item)
    #     validator = ItemValidator(repository)
    #     self.assertRaises(InvalidItemException, lambda: validator.validate(item))
