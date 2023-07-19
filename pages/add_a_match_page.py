from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    main_page_button = "/html/body/div/div[1]/div/div/div/ul[1]/div[1]"
    players_button = "/html/body/div/div[1]/div/div/div/ul[1]/div[2]"
    karol_lausidu_button = "/html/body/div/div[1]/div/div/div/ul[2]/div[1]"
    matches_button = "/html/body/div/div[1]/div/div/div/ul[2]/div[2]"
    reports_button = "/html/body/div/div[1]/div/div/div/ul[2]/div[3]"
    language_button = "/html/body/div/div[1]/div/div/div/ul[3]/div[1]"
    sign_out_button = "/html/body/div/div[1]/div/div/div/ul[3]/div[2]"
    my_team_textbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    enemy_team_textbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_spinbutton = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_spinbutton = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    date_picker = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    match_at_home_radiobutton = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[1]/span[1]/span[1]/input"
    match_out_home_radiobutton = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    T_shirt_color_textbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    league_textbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
    time_played_spinbotton = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    number_spinbotton = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    web_match_texbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    general_textbox = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating_spinbotton = "/html/body/div/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    submit_button = "/html/body/div/div[1]/main/div[2]/form/div[3]/button[1]"
    clear_button = "/html/body/div/div[1]/main/div[2]/form/div[3]/button[2]"
    pass
