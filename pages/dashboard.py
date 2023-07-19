from webdriver_manager.core import driver
from webdriver_manager.core.driver import Driver

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
import time

class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl"
    header_xpath = "/html/body/div/div[1]/header/div/h6"
    main_page_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]"
    players_button_xpath = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]"
    language_button_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_button_xpath = "/html/body/div/div[1]/div/div/div/ul[2]/div[2]"
    add_player_button_xpath = "/html/body/div/div[1]/main/div[3]/div[2]/div/div/a/button"
    dev_team_contact_link_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    last_created_player_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_xpath = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[5]/button"
    wait = WebDriverWait(driver, 15)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.main_page_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_button(self):
        time.sleep(10)
        self.click_on_the_element(self.add_player_button_xpath)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_last_created_player(self):
        self.click_on_the_element(self.last_created_player_xpath)
