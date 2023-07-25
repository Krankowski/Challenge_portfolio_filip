from pages.base_page import BasePage


class LastCreatedPlayer(BasePage):
    matches_button_xpath = "//ul/div[div and div[span[contains(text(), 'Matches')]]]"

    def click_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)

    def wait_for_matches_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.matches_button_xpath)
