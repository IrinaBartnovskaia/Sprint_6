import pytest
import allure
from pages.home_page import HomePage
from data import FAQ

@allure.feature("FAQ")
@allure.story("Выпадающий список 'Вопросы о важном'")
class TestFAQ:
    @allure.title("FAQ: {question}")
    @allure.story("Раздел 'Вопросы о важном'")
    @pytest.mark.parametrize("number, question, expected_answer", FAQ)
    def test_faq(self, driver, number, question, expected_answer):
        homepage = HomePage(driver)
        homepage.open_home_page()
        homepage.close_cookie_banner()

        homepage.click_on_faq(number)
        actual_answer = homepage.get_faq_text_answers(number)

        assert expected_answer == actual_answer