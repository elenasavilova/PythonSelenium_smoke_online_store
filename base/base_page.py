import time
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base class initialization"""

    def __init__(self, driver):
        """Attributes initialization"""
        self.driver = driver

    # methods
    def open_page(self, url):
        """Method that opens url"""
        self.driver.get(url)
        print(f"Open page: {url}")

    # assertions
    def assert_page_url(self, exp_url):
        """Method that check does current page url corresponds to expected url"""
        current_url = self.driver.current_url
        assert current_url == exp_url, f"Page url is {current_url}, expected {exp_url}"


    def assert_page_title(self, locator, exp_title):
        """Method that check does current page title corresponds to expected title"""
        title = WebDriverWait(self.driver, 10).until(visibility_of_element_located((By.XPATH, locator))).text
        assert title == exp_title, print(f"Page title is {title}, expected {exp_title}")

    def take_screenshot(self):
        """Method that takes screenshot"""
        current_datetime = datetime.now().strftime("%d%m%Y-%H%M%S")
        screenshot_name = f'screenshot_{current_datetime}.png'
        self.driver.save_screenshot(f"C:\\Users\\uaaar\\Лена. Обучение\\PythonSelenium_smoke_online_store\\screenshots"
                                    f"\\{screenshot_name}")

    def wait_url_changed(self, old_url):
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != old_url)

    def dynamic_scroll_wait(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    def dynamic_scroll_sleep(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height

