import allure
import pytest
from src.data.tariff import Tariff

class TestTariffs:
    @allure.title("Форма заказа такси открывается и доступны 6 тарифов, Рабочий тариф активен")
    def test_all_tariffs_available_and_work_selected(self, main_page_set_trip):
        main_page_set_trip.assert_all_taxi_types_available()
        main_page_set_trip.assert_taxi_tariff_is_selected(Tariff.WORK)

    @allure.title("Проверка информации о тарифах")
    @pytest.mark.parametrize("taxi_tariff, name, title, description", [
        [Tariff.WORK, "Рабочий", "Для деловых особ, которых отвлекают",
         '— В салоне нет доступа к асоциальным сетям\n— Выдвижной столик для ноутбука'],
        [Tariff.SLEEPY, "Сонный", "Если мысли не выходят из головы",
         "— Вас сопровождает спутник с тремя высшими образованиями\n— Можете обсудить любую тему — от трендов в Тик-токе до квантовой механики"],
        [Tariff.TALKING, "Разговорчивый", "Для тех, кто не выспался",
         "— В салоне кресло-кровать\n— На сиденье мыгкая игрушка — по желанию\n— Водитель ведёт плавно, чтобы вы дремали сладко"],
        [Tariff.COMFORTING, "Утешительный", "Если хочется свернуться калачиком",
         "— В салоне мягкий плед и носовые платки\n— Водитель за звуконепроницаемой шторкой\n— Персональное ведёрко с мороженым"],
        [Tariff.HOLIDAY, "Отпускной", "Если пришла пора отдохнуть",
         "— В салоне массажное кресло\n— В бардачке — расслабляющие маски для лица и патчи."],
        [Tariff.GLOSSY, "Глянцевый", "Если нужно блистать",
         "— В салоне неоновая подсветка\n— С потолка автомобиля непрерывно летят блёстки\n— Салон прошёл верификацию на инстаграммность у лучших экспертов"],
    ])
    def test_tariff_information(self, main_page_set_trip, taxi_tariff, name, title, description):
        main_page_set_trip.click_taxi_tariff(taxi_tariff)
        main_page_set_trip.click_button_taxi_info(taxi_tariff)
        main_page_set_trip.assert_taxi_pop_info(taxi_tariff, name, title, description)
