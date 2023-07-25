from pages.base_page import BasePage


class AddingMatchPlayer(BasePage):
    my_team_texbox_xpath = "//*[@name = 'myTeam']"
    enemy_team_texbox_xpath = "//*[@name = 'enemyTeam']"
    my_team_score_spinbutton_xpath = "//*[@name = 'myTeamScore']"
    enemy_team_score_spinbutton_xpath = "//*[@name = 'enemyTeamScore']"
    date_xpath = "//*[@name = 'date']"
    radio_button_match_at_home_xpath = "//*[@name='matchAtHome' and @value='true']"
    submit_button_xpath = "//*[@type='submit']"

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

    def wait_for_submit_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
