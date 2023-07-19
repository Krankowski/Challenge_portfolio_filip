from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LastCreatedPlayer(BasePage):
    matches_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"

    def click_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)
