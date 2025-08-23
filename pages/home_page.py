import allure
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from curl import Urls

class HomePage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_home_page(self):
        self.open(Urls.MAIN_URL)

    @allure.step("Закрыть баннер куки")
    def close_cookie_banner(self):
        if self.is_element_visible(HomePageLocators.COOKIE_CLOSE_BUTTON):
            self.click(HomePageLocators.COOKIE_CLOSE_BUTTON)

    @allure.step("Кликнуть на кнопку Заказать наверху страницы")
    def click_on_order_button_up(self):
        self.click(HomePageLocators.ORDER_BUTTON_UP)

    @allure.step("Кликнуть на кнопку заказать внизу страницы")
    def click_on_order_button_down(self):
        self.scroll_to_element(HomePageLocators.ORDER_BUTTON_DOWN)
        self.wait_for_element_clickable(HomePageLocators.ORDER_BUTTON_DOWN)
        self.click(HomePageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Кликнуть логотип Яндекс")
    def click_on_logo_yandex(self):
        self.click(HomePageLocators.LOGO_YANDEX_LINK)

    @allure.step("Кликнуть логотип Самокат")
    def click_on_logo_scooter(self):
        self.click(HomePageLocators.LOGO_SCOOTER_LINK)

    @allure.step("Кликнуть на вопрос из FAQ 'Вопросы о важном'")
    def click_on_faq(self, question_number):
            self.scroll_to_element(HomePageLocators.FAQ_QUESTIONS[question_number])
            self.wait_for_element_clickable(HomePageLocators.FAQ_QUESTIONS[question_number])
            self.click(HomePageLocators.FAQ_QUESTIONS[question_number])

    @allure.step("Посмотреть ответ в FAQ 'Вопросы о важном'")
    def get_faq_text_answers(self, answer_number):
        self.wait_visibility(HomePageLocators.FAQ_ANSWERS[answer_number])
        return self.get_text(HomePageLocators.FAQ_ANSWERS[answer_number])

    @allure.step("Проверить, что открыта главная страница")
    def is_home_page_opened(self) -> bool:
        self.wait_visibility(HomePageLocators.ORDER_BUTTON_UP, 10)
        return True

    @allure.step("Переключиться на вкладку Дзена и дождаться загрузки")
    def switch_to_dzen_and_wait(self):
        self.switch_to_another_tab()
        self.wait_for_url_contain("dzen.ru")
