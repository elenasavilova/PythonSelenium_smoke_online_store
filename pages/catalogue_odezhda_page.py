import random
import time

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait
from base.base_page import BasePage


class CataloguePage(BasePage):
    """Class CataloguePage"""

    # Locators
    filter_razmer_odezhdy = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Размер одежды')]/parent::"
                             "div")
    all_razmer_odezhdy = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Размер одежды')]/parent::div/"
                          "following-sibling::div//div[@class='BodyText BodyText--size-large ']")
    filter_tzvet = "//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/parent::div"
    filter_applied = "//div[@class='selectList__overlay']"
    all_tzvet = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/parent::div/following-sibling"
                 "::div//div[@class='catalogFilter__color']/span")
    filter_tzena = "//div[@class='catalogFilter__title-text' and contains(text(), 'Цена')]/parent::div"
    tzena_min = f"//div[@class='TextInput__placeholder' and contains(text(), 'от')]/following-sibling::div/input"
    tzena_max = f"//div[@class='TextInput__placeholder' and contains(text(), 'до')]/following-sibling::div/input"
    primenit_button = ("//div[@class='BodyText BodyText--size-large ' and contains(text(), 'Применить')]/parent::div/"
                       "parent::div")
    items_title = "//div[@class='ProductCard__title']"
    items_price = "//div[@class='ProductCard__price']"
    razmer_odezhdy_cancel = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Размер одежды')]/"
                             "following-sibling::div[@class='catalogFilter__reset']")
    tzvet_cancel = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Цвет')]/following-sibling::div"
                    "[@class='catalogFilter__reset']")
    tzena_cancel = ("//div[@class='catalogFilter__title-text' and contains(text(), 'Цена')]/following-sibling::div"
                    "[@class='catalogFilter__reset']")
    page_title = "//div[@class='TitleText TitleText--size-extra-large CategoryPage__title']"
    item_card = "(//div[@class='catalogCard catalogCard--thin'])[1]"


    # Getters
    def get_filter_razmer_odezhdy(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH,
                                                                             self.filter_razmer_odezhdy)))

    def get_filter_tzvet(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.filter_tzvet)))

    def get_filter_applied(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.filter_applied)))

    def get_filter_tzena(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.filter_tzena)))

    def get_tzena_min(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.tzena_min)))

    def get_tzena_max(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.tzena_max)))

    def get_primenit_button(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.primenit_button)))

    def get_razmer_odezhdy_cancel_btn(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.razmer_odezhdy_cancel)))

    def get_tzvet_cancel_btn(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.tzvet_cancel)))

    def get_tzena_cancel_btn(self):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, self.tzena_cancel)))

    def get_all_items_title(self):
        try:
            return WebDriverWait(self.driver, 15).until(visibility_of_all_elements_located
                                                           ((By.XPATH, self.items_title)))
        except TimeoutException:
            return [] # возвращаем пустой список, если элементы не найдены

    def get_all_items_price(self):
        try:
            return WebDriverWait(self.driver, 15).until(visibility_of_all_elements_located
                                                           ((By.XPATH, self.items_price)))
        except TimeoutException:
            return [] # возвращаем пустой список, если элементы не найдены

    def get_item_card(self):
        return WebDriverWait(self.driver, 5).until(element_to_be_clickable((By.XPATH, self.item_card)))


    # Get lists
    def get_filter_razmer_odezhdy_lst(self):
        """Add available size values from filter 'Размер одежды' to the list"""
        vse_razmery = WebDriverWait(self.driver, 15).until(visibility_of_all_elements_located
                                                           ((By.XPATH, self.all_razmer_odezhdy)))
        razmer_odezhdy_lst = [s.text.strip() for s in vse_razmery]
        return razmer_odezhdy_lst

    def get_filter_tzveta_lst(self):
        """Add available color values from filter 'Цвет' to the list"""
        vse_tzveta = WebDriverWait(self.driver, 15).until(visibility_of_all_elements_located
                                                          ((By.XPATH, self.all_tzvet)))
        return [s.text.strip() for s in vse_tzveta]

    # Get dicts
    def get_items_dict(self):
        """Get all items titles and price, adding them to the dict {title: price}"""

        titles = self.get_all_items_title()
        prices = self.get_all_items_price()

        items_dict = {}
        for title, price in zip(titles, prices):
            try:
                items_dict[title.text] = int(
                    price.text.replace('₽', '').replace(' ', '')
                )
            except StaleElementReferenceException:
                continue

        return items_dict

    # def get_items_dict(self):
    #     """Get all items titles and price, adding them to the dict {title: price}"""
    #
    #     WebDriverWait(self.driver, 20).until(
    #         lambda d: len(d.find_elements(By.XPATH, self.items_title)) > 0
    #     )
    #
    #     titles = self.driver.find_elements(By.XPATH, self.items_title)
    #     prices = self.driver.find_elements(By.XPATH, self.items_price)
    #
    #     items_dict = {}
    #     for title, price in zip(titles, prices):
    #         try:
    #             items_dict[title.text] = int(
    #                 price.text.replace('₽', '').replace(' ', '')
    #             )
    #         except StaleElementReferenceException:
    #             continue
    #
    #     return items_dict

    # def get_items_dict(self):
    #     """Get all items titles and price, adding them to the dict {title: price}"""
    #     all_titles = [i.text for i in self.get_all_items_title()]
    #     all_prices = [int(i.text.replace('₽', '').replace(' ', '')) for i in self.get_all_items_price()]
    #     items_dict = dict(zip(all_titles, all_prices))
    #     return items_dict

    # Get range
    def get_price_range(self):
        """Get min and max price from all downloaded items on the page"""
        prices = self.get_items_dict().values()
        min_price = min(prices)
        max_price = max(prices)
        if min_price == max_price:
            max_price += 1
        return min_price, max_price


    # Locator builder
    def get_razmer_odezhdy_locator(self, value):
        return f"//div[@class='BodyText BodyText--size-large ' and text()='{value}']/parent::div/parent::div"

    def get_tzvet_locator(self, value):
        return f"//span[text()='{value}']/parent::div/parent::div/parent::div/parent::div"

    # Random values
    def get_random_razmer_odezhdy(self):
        """Get random value for filter 'Размер одежды'"""
        sizes = self.get_filter_razmer_odezhdy_lst()
        return random.choice(sizes)


    def get_random_tzvet(self):
        """Get random value for filter 'Цвет'"""
        colors = self.get_filter_tzveta_lst()
        return random.choice(colors)

    def get_random_price_range(self):
        """Ger random range for min and max price"""
        min_price, max_price = self.get_price_range()
        random_min_price = random.randint(min_price, max_price)
        random_max_price = random.randint(random_min_price, max_price)
        print(f"Random range for 'Цена' filter generated, min {random_min_price}, max {random_max_price}")
        return random_min_price, random_max_price


    # Actions
    def open_filter_razmer_odezhdy(self):
        """Click on the filter bytton 'Размер одежды'"""
        self.get_filter_razmer_odezhdy().click()
        print("Click filter 'Размер одежды'")

    def select_random_razmer_odezhdy(self):
        """Select random value from filter 'Размер одежды' values and assert filter applied in URL"""
        value = self.get_random_razmer_odezhdy()
        locator = self.get_razmer_odezhdy_locator(value)
        WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, locator))).click()
        print(f"'Размер одежды': {value} selected")
        self.close_filter_selector() # закрываем фильтр
        return value

    def open_filter_tzveta(self):
        """Click the filter button 'Цвет'"""
        self.get_filter_tzvet().click()
        print("Click filter 'Цвет'")

    def close_filter_selector(self):
        """Click the filter selector"""
        self.get_filter_applied().click()
        print("Close filter selector")

    def select_random_tzveta(self):
        """Select random value from filter 'Цвет' values and assert filter applied in URL"""
        value = self.get_random_tzvet()
        locator = self.get_tzvet_locator(value)
        WebDriverWait(self.driver, 10).until(element_to_be_clickable((By.XPATH, locator))).click()
        print(f"'Цвет': {value} selected")
        self.close_filter_selector() # закрываем фильтр
        return value

    def open_price_filter(self):
        """Click the filter button 'Цена'"""
        self.get_filter_tzena().click()
        print("Click filter 'Цена'")

    def fill_in_min_max_price(self):
        """Enter min and max price for filter 'Цена', assert filters applied in URL"""
        min_price, max_price = self.get_random_price_range()
        self.get_tzena_min().send_keys(str(min_price))
        self.get_tzena_max().send_keys(str(max_price))
        self.click_primenit_button()
        print(f"'Цена': {min_price}-{max_price} selected")
        return min_price, max_price


    def click_primenit_button(self):
        """Click the button 'Применить'"""
        self.get_primenit_button().click()
        print("Click 'Применить' button")

    def reset_razmer_odezhdy_filter(self):
        """Reset 'Размер одежды' filter"""
        self.get_razmer_odezhdy_cancel_btn().click()
        print("Cancel 'Размер одежды' filter")

    def reset_tzvet_filter(self):
        """Reset 'Цвет' filter"""
        self.get_tzvet_cancel_btn().click()
        print("Cancel 'Цвет' filter")

    def reset_tzena_filter(self):
        """Reset 'Цена' filter"""
        self.get_tzena_cancel_btn().click()
        print("Cancel 'Цена' filter")

    def apply_filters_until_items_found(self, open_filter_method, apply_filter_method, reset_filter_method,
                                        assert_method, max_tries=5):
        """Reapply filters in case items aren't found up to max_tries.
        In case of empty result after last try raise AssertionError"""
        old_url = self.driver.current_url

        for i in range(1, max_tries + 1):
            print(f'Try {i} of {max_tries}')

            if i > 1: # начиная со второй попытки сбрасываем фильтр
                reset_filter_method()

                WebDriverWait(self.driver, 20).until(lambda d: d.current_url != old_url)
                old_url = self.driver.current_url
                open_filter_method()

            # применяем фильтр
            applied_value = apply_filter_method()


            # ждём изменения URL
            WebDriverWait(self.driver, 20).until(lambda d: d.current_url != old_url)

            # проверяем URL
            try:
                assert_method(applied_value)
            except AssertionError:
                print("Assert failed, refreshing page")
                self.driver.refresh()
                WebDriverWait(self.driver, 10).until(lambda d: d.current_url != old_url)
                assert_method(applied_value)

            # скролл вниз (динамическая загрузка товаров)
            self.dynamic_scroll_wait()

            # пришлось добавить ожидание, иначе часто словарь собирается до того момента, пока страница окончательно отрендерится
            time.sleep(3)

            # формируем словарь товаров
            items = self.get_items_dict()
            if items:
                print(f"Found {len(items)} items")
                return items


            print("Items not found, reset current filter value")

            old_url = self.driver.current_url

        raise AssertionError("No items found. Finish test")

    def open_card_page(self):
        self.get_item_card().click()







    # Asserts


    def assert_razmer_odezhdy_changed(self, size_value):
        current_url = self.driver.current_url
        if size_value == 'One size':
            assert f"size=One%20size" in current_url, f"Filter {size_value} isn't applied, current url: {current_url}"
            f'Filter: {size_value} applied, current url: {current_url}'
        else:
            assert f'size={size_value}' in current_url, f"Filter {size_value} isn't applied, current url: {current_url}"
            f'Filter: {size_value} applied, current url: {current_url}'

    def assert_tzvet_changed(self, color_value):
        current_url = self.driver.current_url
        assert f"color=" in current_url, f"Filter {color_value} isn't applied, current url: {current_url}"
        # Конкретный id цвета проверить не можем, т.к. id отсутствует в DOM, проверяем, что хотя бы сам фильтр содержится
        # в url
        f'Filter: {color_value} applied, current url: {current_url}'


    def assert_price_changed(self, price_range):
        min_price, max_price = price_range
        current_url = self.driver.current_url

        assert f"price={min_price};{max_price}" in current_url, (f"Filter 'Цена от {min_price} до {max_price}' isn't "
                                                                 f"applied, current url: {current_url}")
        f"Filter 'Цена' от {min_price} до {max_price}' applied, current url: {current_url}"


    # Methods

    def check_page_parameters(self):
        self.assert_page_url("catalog/odezda/womencollection")
        self.assert_page_title(title_xpath=self.page_title, exp_title='Одежда')

    def apply_filters(self):
        # Размер одежды
        self.open_filter_razmer_odezhdy()
        self.apply_filters_until_items_found(open_filter_method=self.open_filter_razmer_odezhdy,
                                             apply_filter_method=self.select_random_razmer_odezhdy,
                                             reset_filter_method=self.reset_razmer_odezhdy_filter,
                                             assert_method=self.assert_razmer_odezhdy_changed, max_tries=5)
        # Цвет
        self.open_filter_tzveta()
        self.apply_filters_until_items_found(open_filter_method=self.open_filter_tzveta,
                                             apply_filter_method=self.select_random_tzveta,
                                             reset_filter_method=self.reset_tzvet_filter,
                                             assert_method=self.assert_tzvet_changed, max_tries=5)

        # Цена
        self.open_price_filter()
        self.apply_filters_until_items_found(open_filter_method=self.open_price_filter,
                                             apply_filter_method=self.fill_in_min_max_price,
                                             reset_filter_method=self.reset_tzena_filter,
                                             assert_method=self.assert_price_changed, max_tries=5)






