from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE

import time
import os


class BasePage():

    def __init__(self, driver: WebDriver) -> object:
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, header_xpath, expected_text):
        element = driver.find_element(by=By.XPATH, value=header_xpath)
        element_text = element.text
        assert expected_text == element_text

    def assert_element_text(self, driver, information_xpath, expected_information_text):
        element = driver.find_element(by=By.XPATH, value=information_xpath)
        element_text = element.text
        assert expected_information_text == element_text

    def assert_element_text(self, driver, edit_header_xpath, edit_expected_text):
        element = driver.find_element(by=By.XPATH, value=edit_header_xpath)
        element_text = element.text
        assert edit_expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(10)

    def wait_for_element_visibility(self, by, value, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, value)))

    def take_screenshot(self, name="screenshot"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_folder = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

        screenshot_path = os.path.join(screenshot_folder, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)