from lab8.domain.CustomerCardValidator import CustomerCardValidator
from lab8.domain.MedicineValidator import MedicineValidator
from lab8.domain.TransactionValidator import TransactionValidator
from lab8.repository.CustomerCardRepository import CustomerCardRepository
from lab8.repository.MedicineRepository import MedicineRepository
from lab8.repository.TransactionRepository import TransactionRepository
from lab8.service.CustomerCardService import CustomerCardService
from lab8.service.MedicineService import MedicineService
from lab8.service.TransactionService import TransactionService
from lab8.user_interface.Console import Console


def main():
    medicine_repository = MedicineRepository("drugs.txt")
    medicine_validator = MedicineValidator()
    customer_card_repository = CustomerCardRepository("cards.txt")
    customer_card_validator = CustomerCardValidator()
    transaction_repository = TransactionRepository("transactions.txt")
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


main()
