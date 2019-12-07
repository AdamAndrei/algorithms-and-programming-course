from domain.CustomerCardValidator import CustomerCardValidator
from domain.MedicineValidator import MedicineValidator
from domain.TransactionValidator import TransactionValidator
from repository.GenericRepository import GenericRepository
from service.CustomerCardService import CustomerCardService
from service.MedicineService import MedicineService
from service.TransactionService import TransactionService
from test.mainTest import run_tests
from user_interface.Console import Console


def main():
    medicine_repository = GenericRepository("drugs.pickle")
    medicine_validator = MedicineValidator()
    customer_card_repository = GenericRepository("cards.pickle")
    customer_card_validator = CustomerCardValidator()
    transaction_repository = GenericRepository("transactions.pickle")
    transaction_validator = TransactionValidator()
    medicine_service = MedicineService(medicine_repository,
                                       medicine_validator,
                                       transaction_repository)
    customer_card_service = CustomerCardService(customer_card_repository,
                                                customer_card_validator,
                                                transaction_repository,
                                                medicine_repository)
    transaction_service = TransactionService(transaction_repository,
                                             transaction_validator,
                                             customer_card_repository,
                                             medicine_repository)
    ui = Console(medicine_service,
                 customer_card_service,
                 transaction_service)
    ui.run_console()


# run_tests()
main()
