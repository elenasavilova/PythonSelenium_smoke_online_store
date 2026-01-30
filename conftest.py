import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up_test():
    print("Start test")

    yield

    print("Finish test")

@pytest.fixture(scope="module")

def driver():
    print("Module")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--guest")
    options.add_argument("--bwsi")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

# @pytest.fixture(scope="module")
# def group():
#     print("Start test module")
#
#     yield
#
#     print("Finish test module")



