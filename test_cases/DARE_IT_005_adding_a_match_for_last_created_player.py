import os
import unittest

from pages.add_a_match_player_page import AddingMatchPlayer
from pages.base_page import BasePage
from pages.last_created_player_page import LastCreatedPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.matches_page import Matches
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestMatchesPage(unittest.TestCase):

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
        dashboard_page.click_last_created_player()

        last_created_player_page = LastCreatedPlayer(self.driver)
        last_created_player_page.wait_for_matches_button_clickability()
        last_created_player_page.click_matches_button()

        matches_page = Matches(self.driver)
        matches_page.wait_for_add_match_button_clickability()
        matches_page.click_add_match_button()

        adding_match_player_page = AddingMatchPlayer(self.driver)
        adding_match_player_page.wait_for_submit_button_clickability()
        adding_match_player_page.type_in_my_team('Coś')
        adding_match_player_page.type_in_enemy_team('Łoś')
        adding_match_player_page.type_in_my_team_score('12')
        adding_match_player_page.type_in_enemy_team_score('8')
        adding_match_player_page.type_in_data('19072023')
        adding_match_player_page.click_match_at_home_radiobutton()
        adding_match_player_page.click_submit_button()

        matches_page.wait_for_add_match_button_clickability()
        matches_page.wait_for_visibility_of_pop_out()


        base_page = BasePage(self.driver)
        base_page.take_screenshot("Screenshot_DARE_IT_005")
        base_page.generate_html_report("DARE_IT_005_html_report")

    @classmethod
    def tearDown(self):
        self.driver.quit()
