import os
import time
import unittest

from pages.base_page import BasePage
from pages.last_created_player_page import LastCreatedPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.marches_page import Matches
from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestMatchesPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_checking_location_of_buttons(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_last_created_player()
        time.sleep(3)
        last_created_player_page = LastCreatedPlayer(self.driver)
        last_created_player_page.click_matches_button()
        time.sleep(3)
        matches_page = Matches(self.driver)
        matches_page.click_add_match_button()
        time.sleep(3)
        matches_page.type_in_my_team('Coś')
        matches_page.type_in_enemy_team('Łoś')
        matches_page.type_in_my_team_score('12')
        matches_page.type_in_enemy_team_score('8')
        matches_page.type_in_data('19072023')
        matches_page.click_match_at_home_radiobutton()
        matches_page.click_submit_button()
        time.sleep(3)

        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_005")

    @classmethod
    def tearDown(self):
        self.driver.quit()
