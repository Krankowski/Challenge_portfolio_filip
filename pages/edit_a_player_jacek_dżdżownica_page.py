from pages.base_page import BasePage

class EditAPlayer(BasePage):
    edit_expected_text = "Edit player Jacek Dżdżownica"
    edit_header_xpath = "/html/body/div/div[1]/main/div[2]/form/div[1]/div/span"

    def title_of_the_header(self):
        self.assert_element_text(self.driver, self.edit_header_xpath, self.edit_expected_text)