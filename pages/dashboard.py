from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "/html/body/div/div[1]/header/div/h6"
    main_page_button = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]"
    players_button = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]"
    language_button = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_button = "/html/body/div/div[1]/div/div/div/ul[2]/div[2]"
    add_player_button = "/html/body/div/div[1]/main/div[3]/div[2]/div/div/a/button"
    dev_team_contact_link = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    last_created_player = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report = "/html/body/div/div[1]/main/div[3]/div[3]/div/div/a[5]/button"
pass