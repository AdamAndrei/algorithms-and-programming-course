import unittest

from lab7.domain.Item import Item
from lab7.domain.ItemValidator import ItemValidator
from lab7.exeption.InvalidItemException import InvalidItemException
from lab7.exeption.ItemNotFoundException import ItemNotFoundException
from lab7.repository.ItemRepository import ItemRepository
from lab7.service.ItemUpdater import ItemUpdater


class ItemUpdaterTest(unittest.TestCase):

    def setUp(self) -> None:
        self.repository = ItemRepository()
        self.updater = ItemUpdater(self.repository, ItemValidator(self.repository))
        item = Item(1, "chair", "made of wood", 23, "room")
        self.repository.add(item)

    def test_update(self):
        updated_item = self.updater.update(1, "table", "made of steel", 34, "roof")
        self.assertEqual("table", updated_item.get_name())
        self.assertEqual("made of steel", updated_item.get_description())
        self.assertEqual(34, updated_item.get_price())
        self.assertEqual("roof", updated_item.get_location())

    def test_update_raises_item_id_not_found_exception(self):
        self.assertRaises(
            ItemNotFoundException,
            lambda: self.updater.update(23253, "table", "made of steel", 34, "roof")
        )

    def test_update_raises_invalid_item_exception_for_empty_name(self):
        self.assertRaises(
            InvalidItemException,
            lambda: self.updater.update(1, "", "made of steel", 34, "roof")
        )





