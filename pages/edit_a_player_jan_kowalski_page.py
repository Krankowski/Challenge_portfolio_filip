from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class EditAPlayer(BasePage):
    edit_expected_text_xpath = "Edit player Jan Kowalski"
    edit_header_xpath = "//span[contains(text(), 'Edit player Jan Kowalski')]"
    pop_out_added_player_xpath = "//div[@role = 'alert' and contains(text(), 'Added player')]"

    def title_of_the_header_and_visibility_of_pop_out(self):
        self.assert_element_text(self.driver, self.edit_header_xpath, self.edit_expected_text_xpath)
        self.wait_for_element_visibility(By.XPATH, self.pop_out_added_player_xpath)