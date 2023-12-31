<span style="color:rgb(174, 211, 97)">
<h1> Task 1: Software configuration </h1>
</span>

## Subtask 1: Why did I choose to participate in the Date IT Challenge?
    
Hi!
My name is Filip, and I'm a would-be PhD student in Food Science and Human Nutrition.
I have always been good with computers, solving problems, etc. so I choose to change something and start a new career.

From not so recent period of time I stared doing some courses in Manual Testing to get into IT word
and gain new skill, mainly to get a useful job. :sweat_smile: I had a small break doing it, but now
I'm back with new energy and motivation!

I thought that learning even the basics of test automatization would help me to get a first job as QA.
It also looks good on CV :grin:

## Subtask 2: Fixing a problem which is shown in the console
I had a problem, not the specific one you presented but similar. On the other hand, the test doesn't work either.
The problem was: "TypeError: WebDriver.__init__() got an unexpected keyword argument 'executable_path'" or something like that.
I have added line 4 and 5 and changed line 14. Fix was found via Google.


## Subtask 3:

Submitted as "first_task" commit.

---
<span style="color:rgb(142, 201, 117)">
<h1> Task 2: Selectors</h1>
</span>

<h2>
<details open>
<summary> Subtask 1: New branch </summary>

Jobs done! :muscle:
</details>
</h2>

## Subtask 2: Searching for selectors on log in's site

<table class="tg">
<thead>
  <tr>
    <th class="tg-3ubz" rowspan="2">Elements</th>
    <th class="tg-k0vl" colspan="3">Selectors</th>
  </tr>
  <tr>
    <th class="tg-49iy">1</th>
    <th class="tg-49iy">2</th>
    <th class="tg-49iy">3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-49iy">Frame</td>
    <td class="tg-vml0">//*[@id="__next"]/form/div</td>
    <td class="tg-vml0">/html/body/div/form/div</td>
    <td class="tg-vml0">//div[contains(@class, "MuiPaper-root")]<br></td>
  </tr>
  <tr>
    <td class="tg-49iy">Heading</td>
    <td class="tg-vml0">//*[@id="__next"]/form/div/div[1]/h5</td>
    <td class="tg-vml0">/html/body/div/form/div/div[1]/h5</td>
    <td class="tg-vml0">//h5[text()="Scouts Panel"]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Textbox - "Login"</td>
    <td class="tg-vml0">//*[@id="login"]</td>
    <td class="tg-vml0">/html/body/div/form/div/div[1]/div[1]/div/input</td>
    <td class="tg-vml0">//*[contains(@id, "login") and (@name="login")]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Textbox - "Password"</td>
    <td class="tg-vml0">//*[@id="password"]</td>
    <td class="tg-vml0">/html/body/div/form/div/div[1]/div[2]/div/input</td>
    <td class="tg-vml0">//*[contains(@name, "password")]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Link - "Remind password"</td>
    <td class="tg-vml0">//*[@id="__next"]/form/div/div[1]/a</td>
    <td class="tg-vml0">/html/body/div/form/div/div[1]/a</td>
    <td class="tg-vml0">//a</td>
  </tr>
  <tr>
    <td class="tg-49iy">Button - "English"</td>
    <td class="tg-vml0">//*[@id="__next"]/form/div/div[2]/div/div</td>
    <td class="tg-vml0">/html/body/div/form/div/div[2]/div/div</td>
    <td class="tg-vml0">//*[text()="English"]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Option - "English"</td>
    <td class="tg-vml0">//*[@id="menu-"]/div[3]/ul/li[2]</td>
    <td class="tg-vml0">/html/body/div[2]/div[3]/ul/li[2]</td>
    <td class="tg-vml0">//child::ul/li[@tabindex="0"]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Option - "Polski"</td>
    <td class="tg-vml0">//*[@id="menu-"]/div[3]/ul/li[1]</td>
    <td class="tg-vml0">/html/body/div[2]/div[3]/ul/li[1]</td>
    <td class="tg-vml0">//child::ul/li[@tabindex="-1"]</td>
  </tr>
  <tr>
    <td class="tg-49iy">Button - "SING IN"</td>
    <td class="tg-vml0">//*[@id="__next"]/form/div/div[2]/button/span[1]</td>
    <td class="tg-vml0">/html/body/div/form/div/div[2]/button/span[1]</td>
    <td class="tg-vml0">//child::button</td>
  </tr>
</tbody>
</table>

## Subtask 3: Adding selectors to the project

<p align="center">
  <img width="300" src="https://github.com/Krankowski/Challenge_portfolio_filip/blob/main/task2%3Bsubtask3.png">
</p>

## Subtask 4: Adding a new file

Jobs done :muscle:

## Subtask 5: Adding a new file - add a match form

```
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

```

## Subtask 6: Branch merging

Done as said!

---

<span style="color:rgb(228, 255, 112)">
<h1> Task 3: First Test and Assert</h1>
</span>

## Subtask 1: Completing The Login Page
I'm kinda to lazy to put like pictures in here while everything is in the files :kissing_heart:  

## Subtask 2: New Test Case

<p align="center">
  <img width="300" src="https://github.com/Krankowski/Challenge_portfolio_filip/blob/main/tutorial.jpg">
</p>

## Subtask 3: Assert

I struggled a bit, but it worked!

## Subtask 4: Reiteration of What We Already Know

Piece of cake :blush:

## Subtask 5: Optional Task (to be done independently or in a group)

ChatGPT is a great source of knowledge and assistance!


## Subtask 6: Branch merging

Done as said!

---

<span style="color:rgb(255, 153, 153)">
<h1> Task 4: Refactor, debugger and test cases</h1>
</span>

## Subtask 1: Writing test cases

Done as said, everything is on the GoogleDrive. Check here: [Google Drive](https://docs.google.com/spreadsheets/d/1pifEBBpws1hr4d87H7uo2_fC_H-OaJZI/edit?usp=sharing&ouid=103846351617777504097&rtpof=true&sd=true)

## Subtask 2: Writing code based on test cases

With a little bit of difficulties, I managed to do so as intended.

## Subtask 3: Adding recordings of running tests to google drive.

Everything is on the GoogleDrive. Same thing here as in subtask1. [Google Drive](https://drive.google.com/drive/folders/1yNEGEKu426Oypud9SVf7aHwpX_rPjDB4?usp=sharing)

## Subtask 4: Screenshot method and test report - for willing and for groups

All done!

## Subtask 5: For volunteers → Construction of if else

Unfortunately not today...

---

<span style="color:rgb(228, 255, 112)">
<h1> Task 6: Reporting bugs, and test report</h1>
</span>

## Subtask 1: Changing the environment

Done. You can check that in test case file in PyCharm.

## Subtask 2: Bug reports

Just check: [Click here](https://docs.google.com/spreadsheets/d/1WrRHS5MspB1v2q9ZoLHysYhJYk_wq266ldXCoKdnvsM/edit?usp=sharing)

## Subtask 3: Test report

Just check: [Click here](https://docs.google.com/document/d/1ZB7R0mgGCFgMhTE98pXO7hrcCS1b0e6Xp49ZrNMZz1A/edit?usp=sharing)
