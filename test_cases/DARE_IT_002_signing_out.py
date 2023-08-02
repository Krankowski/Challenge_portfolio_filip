import os
import unittest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestDashboardPage_1(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://dareit.futbolkolektyw.pl/en/login?redirected=true')
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_signing_out(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page_and_clickability()
        dashboard_page.click_sign_out_button()

        user_login.title_of_page_and_clickability()

        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_002")
        base_page.generate_html_report("DARE_IT_002_html_report")

    @classmethod
    def tearDown(self):
        self.driver.quit()
