from pages.base_page import BasePage


class PlayersPage(BasePage):
    players_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    expected_title_suffix = "Players"
    name_button_xpath = "//button[span/div/div[contains(text(), 'Name')]]"
    surname_button_xpath = "//button[span/div/div[contains(text(), 'Surname')]]"
    age_button_xpath = "//button[span/div/div[contains(text(), 'Age')]]"
    main_position_button_xpath = "//button[span/div/div[contains(text(), 'Main position')]]"
    club_button_xpath = "//button[span/div/div[contains(text(), 'Club')]]"
    rating_button_xpath = "//button[span/div/div[contains(text(), 'Rating')]]"

    def title_of_page(
            self):  # Compares the "get" title of the page to the expected title which changes but always starts with "Players"
        assert self.get_page_title(self.players_url).startswith(self.expected_title_suffix)

    def wait_for_name_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.name_button_xpath)

    def wait_for_surname_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.surname_button_xpath)

    def wait_for_age_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.age_button_xpath)

    def wait_for_main_position_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.main_position_button_xpath)

    def wait_for_club_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.club_button_xpath)

    def wait_for_rating_button_clickability(self):
        self.wait_for_element_to_be_clickable(self.rating_button_xpath)
