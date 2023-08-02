import os
import unittest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.players_page import PlayersPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestPlayersPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_checking_location_of_buttons(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page_and_clickability()
        dashboard_page.click_players_button()

        player_page = PlayersPage(self.driver)
        player_page.title_of_page()
        player_page.wait_for_name_button_clickability()
        player_page.wait_for_surname_button_clickability()
        player_page.wait_for_age_button_clickability()
        player_page.wait_for_main_position_button_clickability()
        player_page.wait_for_club_button_clickability()
        player_page.wait_for_rating_button_clickability()

        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_004")
        base_page.generate_html_report("DARE_IT_004_html_report")

    @classmethod
    def tearDown(self):
        self.driver.quit()
