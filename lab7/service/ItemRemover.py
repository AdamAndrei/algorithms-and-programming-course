from lab7.domain.ItemValidator import ItemValidator
from lab7.exeption.ItemNotFoundException import ItemNotFoundException
from lab7.repository.ItemRepository import ItemRepository


class ItemRemover:
    def __init__(self, item_repository: ItemRepository, item_validator: ItemValidator):
        self.__item_repository = item_repository
        self.__item_validator = item_validator

    def remove(self, item_id: int):
        item = self.__item_repository.find_by_id(item_id)
        if item is None:
            raise ItemNotFoundException("Item with id {} does not exists".format(item_id))
        del item
