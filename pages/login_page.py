from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    login_url = "https://scouts-test.futbolkolektyw.pl/en/login?redirected=true"
    expected_title = "Scouts panel - sign in"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    header_xpath = "//h5[text()='Scouts Panel']"
    expected_text = "Scouts Panel"
    information_xpath = "//*[text()='Identifier or password invalid.']"
    expected_information_text = "Identifier or password invalid."
    driver = webdriver.Chrome()
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page_and_clickability(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_the_header(self):
        self.assert_element_text(self.driver, self.header_xpath, self.expected_text)

    def wait_for_visibility_of_the_information(self):
        self.wait_for_element_visibility(By.XPATH, self.information_xpath)

    def title_of_the_information(self):
        self.assert_element_text(self.driver, self.information_xpath, self.expected_information_text)

