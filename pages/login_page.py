from pages.base_page import BasePage


class LoginPage(BasePage):
    main_frame_xpath = "//div[contains(@class, 'MuiPaper-root')]"
    header_xpath = "//h5[text()='Scouts Panel']"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[contains(@name, 'password')]"
    remind_password_link_xpath = "//a"
    english_button_xpath = "//*[text()='English']"
    english_option_xpath = "//child::ul/li[@tabindex='0']"
    polski_option_xpath = "//child::ul/li[@tabindex='-1']"
    sign_in_button_xpath = "//child::button"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
