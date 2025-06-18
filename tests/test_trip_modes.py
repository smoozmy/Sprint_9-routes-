import allure
from src.data.trip_mode import TripMode
from src.data.trip_type import TripType

class TestTripModes:
    POINT_A = "Хамовнический Вал, 34"
    POINT_B = "Зубовский бульвар, 37"

    @allure.title("В 'Свой' режиме доступны все типы передвижения")
    def test_own_mode_all_trip_types(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_B)
        main_page.switch_mode(TripMode.OWN)
        main_page.assert_selected_tab(TripMode.OWN)
        main_page.assert_all_trip_types_available()

    @allure.title("Кнопка 'Вызвать такси' доступна в Быстром режиме")
    def test_fast_mode_taxi_button_visible(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_B)
        main_page.switch_mode(TripMode.FAST)
        main_page.assert_selected_tab(TripMode.FAST)
        main_page.assert_button_call_taxi_is_visible()

    @allure.title("Кнопка 'Забронировать' доступна в режиме 'Свой' с типом 'Драйв'")
    def test_drive_type_book_button_visible(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_B)
        main_page.switch_mode(TripMode.OWN)
        main_page.assert_selected_tab(TripMode.OWN)
        main_page.click_button_trip_type(TripType.DRIVE)
        main_page.assert_button_book_is_visible()
