import os
import time
import unittest

from pages.add_a_player_page import AddAPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_a_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_button()
        time.sleep(5)

        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.title_of_the_page()

        #add_player_page = AddAPlayer(self.driver)
        #add_player_page.type_in_name('Jan')
        #add_player_page.type_in_surname('Kowalski')
        #add_player_page.type_in_main_position('Obrońca')
        #add_player_page.type_in_the_age_data_picker('02031998')
        #add_player_page.click_on_the_submit_button()
        #time.sleep(5)



    @classmethod
    def tearDown(self):
        self.driver.quit()