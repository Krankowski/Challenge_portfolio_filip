import os
import unittest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system_with_wrong_password(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('test')
        user_login.click_on_the_sign_in_button()
        user_login.wait_for_visibility_of_the_information()
        user_login.title_of_the_information()

        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_001")
        base_page.generate_html_report("DARE_IT_001_html_report")

    @classmethod
    def tearDown(self):
        self.driver.quit()
