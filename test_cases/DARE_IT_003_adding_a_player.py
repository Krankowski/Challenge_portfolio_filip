import os
import time
import unittest

from pages.add_a_player_page import AddAPlayer
from pages.base_page import BasePage
from pages.edit_a_player_jacek_dżdżownica_page import EditAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()

        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.title_of_the_page()
        add_a_player_page.type_in_email('test@gmail.com')
        add_a_player_page.type_in_name('Jacek')
        add_a_player_page.type_in_surname('Dżdżownica')
        add_a_player_page.type_in_phone('789 456 123')
        add_a_player_page.type_in_weight("80")
        add_a_player_page.type_in_height("190")
        add_a_player_page.type_in_the_age_data_picker('02031998')
        add_a_player_page.type_in_main_position('defender')
        add_a_player_page.click_on_the_submit_button()
        time.sleep(10)
        edit_a_player_page_jacek_dżdżownica_page = EditAPlayer(self.driver)
        edit_a_player_page_jacek_dżdżownica_page.title_of_the_header()

        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_003")

    @classmethod
    def tearDown(self):
        self.driver.quit()
