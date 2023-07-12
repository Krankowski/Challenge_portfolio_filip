from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    name_texbox_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_texbox_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    age_data_picker_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    main_position_texbox_xpath = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    submit_button_xpath = "/html/body/div/div[1]/main/div[2]/form/div[3]/button[1]"
    saved_player_alart_xpath = "/html/body/div/div[2]/div/div/div[1]"

    def type_in_name(self, name):
        self.field_send_keys(self.name_texbox_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_texbox_xpath, surname)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_texbox_xpath, main_position)

    def type_in_the_age_data_picker(self, age):
        self.field_send_keys(self.age_data_picker_xpath, age)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_the_page(self):
        assert self.get_page_title(self.add_a_player_url) == self.expected_title
