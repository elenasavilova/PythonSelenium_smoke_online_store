from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.catalogue_odezhda_page import CataloguePage
from pages.main_page import MainPage


def test_open_catalogue():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options._arguments = ["--bwsi", "--guest", "--start-maximized"]
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    # class instantiation
    main_page = MainPage(driver)
    catalogue_page = CataloguePage(driver)

    # test
    main_page.select_smotret_vse()
    catalogue_page.check_page_parameters()
    catalogue_page.apply_filters()




