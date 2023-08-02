from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_a_player_url = "https://dareit.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    email_textbox_xpath = "//*[@name='email']"
    name_texbox_xpath = "//*[@name='name']"
    surname_texbox_xpath = "//*[@name='surname']"
    phone_texbox_xpath = "//*[@name='phone']"
    weight_spinbutton_xpath = "//*[@name='weight']"
    height_spinbutton_xpath = "//*[@name='height']"
    age_data_picker_xpath = "//*[@name='age']"
    main_position_texbox_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type = 'submit']"

    def title_of_the_page_and_clickability(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_textbox_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_texbox_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_texbox_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_texbox_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_spinbutton_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_spinbutton_xpath, height)

    def type_in_the_age_data_picker(self, age_data):
        self.field_send_keys(self.age_data_picker_xpath, age_data)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_texbox_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)
