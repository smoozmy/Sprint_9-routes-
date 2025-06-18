import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from src.urls import BASE_URL
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def main_page_set_trip(driver):
    main_page = MainPage(driver)
    main_page.type_route("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    main_page.click_button_call_taxi()
    return main_page