from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PlayersPage(BasePage):
    name_button_xpath = "/html/body/div/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[1]/span/button"
    surname_button_xpath = "/html/body/div/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[2]/span/button"
    age_button_xpath = "/html/body/div/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[3]/span/button"

    def wait_for_name_button_visibility(self):
        self.wait_for_element_visibility(By.XPATH, self.name_button_xpath)

    def wait_for_surname_button_visibility(self):
        self.wait_for_element_visibility(By.XPATH, self.surname_button_xpath)

    def wait_for_age_button_visibility(self):
        self.wait_for_element_visibility(By.XPATH, self.age_button_xpath)
