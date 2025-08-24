import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import TestData

@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий: заполнение формы и подтверждение")
class TestOrderScooter:
    @allure.title("Позитивный сценарий заказа (кнопка: {click_btn_id})")
    @pytest.mark.parametrize(
        "user, click_btn, click_btn_id",
        [
            (TestData.USER_1, HomePage.click_on_order_button_up, "up"),
            (TestData.USER_2, HomePage.click_on_order_button_down, "down"),
        ]
    )
    def test_order_scooter_with_order_buttons_positive_flow(self, driver, user, click_btn, click_btn_id):
        home = HomePage(driver)
        order = OrderPage(driver)

        home.open_home_page()
        home.close_cookie_banner()

        click_btn(home)

        order.fill_first_step(user)
        order.fill_second_step(user)

        order.confirm_order()
        assert order.is_order_placed()
        assert TestData.SUCCESSFUL_MESSAGE in order.get_success_message()