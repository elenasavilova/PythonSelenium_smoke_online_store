import random
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located, \
    presence_of_element_located, visibility_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options._arguments = ["--bwsi", "--guest", "--start-maximized"]
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
base_url = "https://12storeez.com/catalog/odezda/womencollection"
driver.get(base_url)
WebDriverWait(driver, 120).until(element_to_be_clickable(
    (By.XPATH, "(//div[@class='popmechanic-close popmechanic-close-icon'])[1]"))).click()
# menu = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH,"//div[@class='HeaderMenuButton HeaderMenuButton--white']")))
# ActionChains(driver).move_to_element(menu).perform()
# odezhda = WebDriverWait(driver, 10).until(visibility_of_element_located((By.XPATH, "//div[@class='MenuItem__text' and contains(text(), 'Одежда')]/parent::div")))
# ActionChains(driver).move_to_element(odezhda).perform()
# smotret_vse = WebDriverWait(driver, 10).until(visibility_of_element_located((By.XPATH, "(//div[@class='MenuItem__text' and contains(text(), 'Смотреть все')])[2]")))
# ActionChains(driver).move_to_element(smotret_vse).click().perform()
# #
WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "//div[@class='catalogFilter__title-text' and contains(text(), 'Размер одежды')]/parent::div"))).click()
WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "//div[@class='BodyText BodyText--size-large ' and contains(text(), 'XXL')]/parent::div/parent::div"))).click()
WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/parent::div"))).click()
WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Принт')]//ancestor::div[@class='selectList__item selectList__item--icon-right']"))).click()

# vse_razmery = WebDriverWait(driver, 10).until(visibility_of_all_elements_located((By.XPATH, "//div[@class='catalogFilter__title-text' and contains(text(), 'Размер одежды')]/parent::div/following-sibling::div//div[@class='BodyText BodyText--size-large ']")))
# razmer_odezhdy_lst = [s.text.strip() for s in vse_razmery]
# size = random.choice(razmer_odezhdy_lst)
# locator = f"//div[@class='BodyText BodyText--size-large ' and text()='{size}']/parent::div/parent::div"
# print(size)
# WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, locator))).click()
time.sleep(5)
items_title = "//div[@class='ProductCard__title']"
items_price = "//div[@class='ProductCard__price']"


def get_all_items_title():
    try:
        return WebDriverWait(driver, 30).until(visibility_of_all_elements_located
                                                    ((By.XPATH, items_title)))
    except TimeoutException:
        return ''  # уточнить эту строку


def get_all_items_price():
    try:
        return WebDriverWait(driver, 10).until(visibility_of_all_elements_located
                                                    ((By.XPATH, items_price)))
    except TimeoutException:
        return ''  # уточнить строку

def get_items_dict():
    all_titles = [i.text for i in get_all_items_title()]
    all_prices = [int(i.text.replace('₽', '').replace(' ', '')) for i in get_all_items_price()]
    items_dict = dict(zip(all_titles, all_prices))
    print(items_dict)

get_items_dict()


# WebDriverWait(driver, 10).until(element_to_be_clickable((By.XPATH, "//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/parent::div"))).click()
#
# vse_tzveta = WebDriverWait(driver, 10).until(visibility_of_all_elements_located((By.XPATH, "//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/parent::div/following-sibling"
#                  "::div//div[@class='catalogFilter__color']/span")))
# vse_tzveta_dict = {index: value for index, value in enumerate(v.text.split() for v in vse_tzveta)}
# print(vse_tzveta_dict)
#
#
# colors_dict = {3: 'Бежевый', 1: 'Белый', 4: 'Голубой', 5: 'Желтый', 6: 'Зеленый', 8: 'Коричневый',
#                9: 'Кофейный', 13: 'Красный', 16: 'Металлик', 7: 'Молочный', 14: 'Оливковый',
#                12: 'Оранжевый', 15: 'Принт', 11: 'Розовый', 10: 'Серый', 17: 'Синий', 18: 'Фиолетовый',
#                2: 'Черный'}
#
# colors_dict = {value: index for index ,value in colors_dict.items()}
# print(colors_dict)
#
# print(colors_dict['Бежевый'])
# all_titles = [i.text for i in WebDriverWait(driver, 10).until(visibility_of_all_elements_located
#                                                   ((By.XPATH, "//div[@class='ProductCard__title']")))]
# all_prices = [int(i.text.replace('₽', '').replace(' ', ''))for i in WebDriverWait(driver, 10).until(visibility_of_all_elements_located
#                                                   ((By.XPATH, "//div[@class='ProductCard__price']")))]
# items_dict = dict(zip(all_titles, all_prices))
# print(items_dict)

