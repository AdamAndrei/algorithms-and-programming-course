import unittest

from test.domainTest.CustomerCardTest import CustomerCardTest
from test.domainTest.MedcineTest import MedicineTest
from test.domainTest.TransactionTest import TransactionTest
from test.repositoryTest.GenericRepositoryTest import GenericRepositoryTest
from test.serviceTest.CustomerCardServiceTest import CustomerCardServiceTest
from test.serviceTest.MedicineServiceTest import MedicineServiceTest
from test.serviceTest.TransactionServiceTest import TransactionServiceTest


def run_tests():
    loader = unittest.defaultTestLoader
    all_suites = \
        [
            loader.loadTestsFromTestCase(MedicineServiceTest),
            loader.loadTestsFromTestCase(MedicineTest),
            loader.loadTestsFromTestCase(CustomerCardTest),
            loader.loadTestsFromTestCase(TransactionTest),
            loader.loadTestsFromTestCase(CustomerCardServiceTest),
            loader.loadTestsFromTestCase(TransactionServiceTest),
            loader.loadTestsFromTestCase(GenericRepositoryTest)
        ]
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(unittest.TestSuite(all_suites))


if __name__ == '__main__':
    run_tests()
