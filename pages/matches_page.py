from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Matches(BasePage):
    add_match_button_xpath = "/html/body/div/div[1]/main/a/button"
    pop_out_added_match_xpath = "//div[@role = 'alert' and contains(text(), 'Added match')]"

    def click_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def wait_for_add_match_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)

    def wait_for_visibility_of_pop_out(self):
        self.wait_for_element_visibility(By.XPATH, self.pop_out_added_match_xpath)