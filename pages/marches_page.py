from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Matches(BasePage):
    add_match_button_xpath = "/html/body/div/div[1]/main/a/button"
    my_team_texbox_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_texbox_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_spinbutton_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_spinbutton_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    date_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    radio_button_match_at_home_xpath = "//input[@name='matchAtHome' and @type='radio' and @value='true']"
    submit_button_xpath = "/html/body/div/div[1]/main/div[2]/form/div[3]/button[1]"
    def click_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def type_in_my_team(self, my_team):
        self.field_send_keys(self.my_team_texbox_xpath, my_team)

    def type_in_enemy_team(self, enemy_team):
        self.field_send_keys(self.enemy_team_texbox_xpath, enemy_team)

    def type_in_my_team_score(self, my_team_score):
        self.field_send_keys(self.my_team_score_spinbutton_xpath, my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
            self.field_send_keys(self.enemy_team_score_spinbutton_xpath, enemy_team_score)

    def type_in_data(self, data):
        self.field_send_keys(self.date_xpath, data)

    def click_match_at_home_radiobutton(self):
        self.click_on_the_element(self.radio_button_match_at_home_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

