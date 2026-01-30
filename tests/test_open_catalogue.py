from pages.catalogue_odezhda_page import CataloguePage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_open_catalogue():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--guest")
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    service = Service(r"C:\Users\Sasha\Alena\PythonSelenium_Online_store\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    main_page = MainPage(driver)
    catalogue_page = CataloguePage(driver)

    main_page.open_page(MainPage.base_url)
    main_page.select_smotret_vse()

    catalogue_page.check_page_parameters()
    catalogue_page.apply_filters()

test_open_catalogue()



