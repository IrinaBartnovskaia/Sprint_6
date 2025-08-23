import allure
from pages.home_page import HomePage



@allure.feature("Навигация")
@allure.story("Переходы по логотипам на главной странице")
class TestNavigation:
    @allure.title("Клик по логотипу Самоката возвращает на главную страницу")
    def test_click_on_logo_scooter_redirect_to_main_page(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()
        home_page.close_cookie_banner()

        home_page.click_on_order_button_up()
        home_page.click_on_logo_scooter()

        assert home_page.is_home_page_opened()

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_click_on_logo_yandex_redirect_to_dzen(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()
        home_page.close_cookie_banner()

        home_page.click_on_logo_yandex()
        home_page.switch_to_dzen_and_wait()

        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url