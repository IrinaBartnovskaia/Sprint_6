import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    @allure.step("Ввести имя: {name}")
    def set_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)

    @allure.step("Ввести фамилию: {surname}")
    def set_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step("Ввести адрес: {address}")
    def set_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step("Выбрать станцию метро")
    def set_metro_station(self, station_name: str):
        field = self.wait_visibility(OrderPageLocators.METRO_FIELD, 10)
        field.click()
        field.clear()
        field.send_keys(station_name[:3])
        self.wait_visibility(OrderPageLocators.METRO_OPTIONS, 5)
        field.send_keys(Keys.ARROW_DOWN)
        field.send_keys(Keys.ENTER)

    @allure.step("Нажать «Далее» (шаг 1)")
    def click_next_button(self):
        self.wait_for_element_clickable(OrderPageLocators.NEXT_BUTTON, timeout=10)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Ввести телефон: {phone}")
    def set_phone(self, phone):
        self.wait_visibility(OrderPageLocators.PHONE_FIELD, timeout=15)
        self.scroll_to_element(OrderPageLocators.PHONE_FIELD)
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone, timeout=15)

    @allure.step("Нажать Далее")
    def click_next_button(self):
        self.wait_for_element_clickable(OrderPageLocators.BUTTON_NEXT, timeout=10)
        self.click(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Указать дату доставки")
    def set_delivery_date(self, date_str: str):
        field = self.wait_visibility(OrderPageLocators.DELIVERY_DATE, 10)
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(date_str)
        field.send_keys(Keys.ENTER)
        self.wait_invisibility(OrderPageLocators.DATEPICKER_OVERLAY, 5)

    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, period_name):
        self.wait_for_element_clickable(OrderPageLocators.RENTAL_PERIOD_FIELD, 5)
        self.click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        period_locators = {
            "сутки": OrderPageLocators.RENTAL_PERIOD_ONE_DAY,
            "двое суток": OrderPageLocators.RENTAL_PERIOD_TWO_DAYS
        }
        self.click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click(period_locators[period_name])

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color_name):
        color_locators = {
            "black": OrderPageLocators.SCOOTER_BLACK_CHECKBOX,
            "grey": OrderPageLocators.SCOOTER_GREY_CHECKBOX
        }
        self.click(color_locators[color_name])

    @allure.step("Выбрать срок аренды: {period}")
    def set_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click(OrderPageLocators.RENTAL_OPTIONS[period])

    @allure.step("Добавить комментарий курьеру: {comment}")
    def set_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_element_clickable(OrderPageLocators.ORDER_BUTTON, 10)
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.wait_visibility(OrderPageLocators.CONFIRM_BUTTON, 10)
        self.wait_for_element_clickable(OrderPageLocators.CONFIRM_BUTTON, 10)
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        self.wait_visibility(OrderPageLocators.SUCCESS_MODAL, 10)

    @allure.step("Заполнить первый шаг формы заказа")
    def fill_first_step(self, user: dict):
        self.set_name(user["name"])
        self.set_surname(user["surname"])
        self.set_address(user["address"])
        self.set_metro_station(user["metro_station"])
        self.set_phone(user["telephone"])
        self.click_next_button()
        self.wait_visibility(OrderPageLocators.SECOND_STEP_HEADER, 10)

    @allure.step("Заполнить второй шаг формы заказа")
    def fill_second_step(self, user: dict):
        self.set_delivery_date(user["delivery_date"])
        self.set_rental_period(user["rental_period"])
        self.select_scooter_color(user["scooter_color"])
        self.set_comment(user["comment"])

    @allure.step("Проверить, что заказ оформлен")
    def is_order_placed(self):
        return self.is_element_visible(OrderPageLocators.HEADER_SUCCESS)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.HEADER_SUCCESS)