from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class initialization"""

    def __init__(self, driver):
        """Attributes initialization"""
        self.driver = driver


    # methods

    def get_page_title(self, locator):
        """Method that return page title"""
        try:
            title = WebDriverWait(self.driver, 10).until(visibility_of_element_located((By.XPATH, locator)))
            return title.text

        except TimeoutException:
            return print("Element isn't found")


    def assert_page_url(self, exp_url):
        """Method that check does current page url corresponds to expected url"""
        try:
            current_url = self.driver.current_url
            assert current_url == exp_url
            print("OK. Current URL is correct")

        except AssertionError:
            print(f"Page url is {current_url}, expected {exp_url}")

    def assert_page_title(self, exp_title):
        """Method that check does current page title corresponds to expected title"""
        try:
            title = self.get_page_title(locator).text



