from lab7.domain.ItemValidator import ItemValidator
from lab7.exeption.ItemNotFoundException import ItemNotFoundException
from lab7.repository.ItemRepository import ItemRepository


class ItemUpdater:
    def __init__(self, item_repository: ItemRepository, item_validator: ItemValidator):
        self.__item_repository = item_repository
        self.__item_validator = item_validator

    def update(self, item_id, new_name, new_description, new_price, new_location):
        item = self.__item_repository.find_by_id(item_id)
        if item is None:
            raise ItemNotFoundException("Item with id {} does not exists".format(item_id))
        item.set_name(new_name)
        item.set_description(new_description)
        item.set_price(new_price)
        item.set_location(new_location)
        self.__item_validator.validate(item)

        return item
