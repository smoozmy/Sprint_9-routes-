import allure

class TestRouteDisplay:
    POINT_A = "Хамовнический Вал, 34"
    POINT_B = "Зубовский бульвар, 37"

    @allure.title("Точки начала и конца маршрута видны на карте, если указать маршрут")
    def test_points_visible_on_map(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_B)
        main_page.assert_start_point_a_visible(self.POINT_A)
        main_page.assert_start_point_b_visible(self.POINT_B)

    @allure.title("Блок-меню выбора маршрута виден слева от карты, если указать маршрут")
    def test_route_picker_menu_visible(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_B)
        main_page.assert_route_picker_menu_is_visible()

    @allure.title("Ввести одинаковый адрес в 'Откуда' и 'Куда', блок-меню показывает текст бесплатно")
    def test_same_point_free_trip_text(self, main_page):
        main_page.type_route(self.POINT_A, self.POINT_A)
        main_page.assert_free_trip()
