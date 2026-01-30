from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from base.base_page import BasePage

class MainPage(BasePage):
    """Class for opening main page"""
    base_url = "https://12storeez.com/"

    # Locators
    header_menu_button = "//div[@class='HeaderMenuButton HeaderMenuButton--white']"
    menu_item_odezhda = "//div[@class='MenuItem__text' and contains(text(), 'Одежда')]/parent::div"
    menu_item_smotret_vse = "(//div[@class='MenuItem__text' and contains(text(), 'Смотреть все')])[2]"
    close_popup_button = "(//div[@class='popmechanic-close popmechanic-close-icon'])[1]"

    # Getters
    def get_header_menu_button(self):
        return WebDriverWait(self.driver, 30).until(element_to_be_clickable((By.XPATH, self.header_menu_button)))

    def get_menu_item_odezhda(self):
        return WebDriverWait(self.driver, 30).until(element_to_be_clickable((By.XPATH, self.menu_item_odezhda)))

    def get_menu_item_smotret_vse(self):
        return WebDriverWait(self.driver, 30).until(element_to_be_clickable((By.XPATH, self.menu_item_smotret_vse)))


    # Actions

    def close_popup(self):
        try:
            WebDriverWait(self.driver, 120).until(
                element_to_be_clickable((By.XPATH, self.close_popup_button))
            ).click()
            print("Close popup")
        except TimeoutException:
            print("Popup is not found")

    def hover_header_menu_button(self):
        ActionChains(self.driver).move_to_element(self.get_header_menu_button()).perform()
        print("Hover the header menu button")

    def hover_odezhda_menu_item(self):
        ActionChains(self.driver).move_to_element(self.get_menu_item_odezhda()).perform()
        print("Hover 'Одежда' menu item")

    def smotret_vse_click(self):
        ActionChains(self.driver).move_to_element(self.get_menu_item_smotret_vse()).click().perform()
        print("Hover 'Смотреть все' menu item and click")

    # Methods
    def open_main_page(self):
        self.open_page(self.base_url)
    def select_smotret_vse(self):
        self.close_popup()
        self.hover_header_menu_button()
        self.hover_odezhda_menu_item()
        self.smotret_vse_click()


