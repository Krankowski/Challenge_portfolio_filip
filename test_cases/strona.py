import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
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
        time.sleep(10)
        dashboard_page.click_players_button()

        # Pobierz i wydrukuj tytuł strony po zalogowaniu
        def get_and_print_title_with_selenium(driver, url):
            try:
                driver.get(url)
                title = driver.title
                print("Title:", title)
            except Exception as e:
                print("Error:", e)

        # Przykład użycia
        url_after_login = "https://dareit.futbolkolektyw.pl/en/players"  # Zastąp tym adresem URL strony po zalogowaniu
        get_and_print_title_with_selenium(self.driver, url_after_login)

if __name__ == "__main__":
    unittest.main()
