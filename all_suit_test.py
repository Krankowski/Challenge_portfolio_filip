import unittest

from test_cases.DARE_IT_001_wrong_password import TestLoginPage
from test_cases.DARE_IT_002_Signing_out import TestDashboardPage_1
from test_cases.DARE_IT_003_adding_a_player import TestDashboardPage_2
from test_cases.DARE_IT_004_checking_location_of_buttons import TestPlayersPage
from test_cases.DARE_IT_005_adding_a_match_for_last_created_player import TestMatchesPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestLoginPage))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDashboardPage_1))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestDashboardPage_2))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestPlayersPage))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TestMatchesPage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
