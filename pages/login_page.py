from pages.base_page import BasePage
from selenium import webdriver

class LoginPage(BasePage):
    driver = webdriver.Chrome()
    main_frame_xpath = "//div[contains(@class, 'MuiPaper-root')]"
    login_field_xpath = "//*[@id='login']"
    login_url = "https://scouts-test.futbolkolektyw.pl/en/login?redirected=true"
    expected_title = "Scouts panel - sign in"
    password_field_xpath = "//*[contains(@name, 'password')]"
    remind_password_link_xpath = "//a"
    english_button_xpath = "//*[text()='English']"
    english_option_xpath = "//child::ul/li[@tabindex='0']"
    polski_option_xpath = "//child::ul/li[@tabindex='-1']"
    sign_in_button_xpath = "//child::button"
    header_xpath = "//h5[text()='Scouts Panel']"
    expected_text = "Scouts Panel"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def title_of_the_header(self):
        self.assert_element_text(self.driver, self.header_xpath, self.expected_text)