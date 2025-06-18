import allure
import pytest
from src.data.tariff import Tariff

class TestTaxiOrder:
    @allure.title("Заказ такси с отображением формы ожидания")
    def test_order_taxi_shows_search_form(self, main_page_set_trip):
        main_page_set_trip.click_taxi_tariff(Tariff.WORK)
        main_page_set_trip.open_form_request_to_taxi_order()
        main_page_set_trip.click_button_order_taxi()
        main_page_set_trip.assert_taxi_searching_form_is_visible()

    @pytest.mark.xfail(reason="Кнопка 'Отменить' не работает")
    @allure.title("Заказ и отмена такси")
    def test_order_and_cancel(self, main_page_set_trip):
        page = main_page_set_trip
        page.click_taxi_tariff(Tariff.WORK)
        page.open_form_request_to_taxi_order()
        page.click_button_order_taxi()
        page.assert_taxi_searching_form_is_visible()
        page.click_button_cancel_order_taxi()
        page.order_form_is_closed()
