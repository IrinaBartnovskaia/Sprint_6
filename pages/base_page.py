import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ждать видимость элемента")
    def wait_visibility(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ждать, пока элемент станет кликабельным")
    def wait_for_element_clickable(self,locator, timeout = 5):
        return WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Переключиться на другую вкладку")
    def switch_to_another_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получить текущий адрес страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать загрузку страницы")
    def wait_for_url_contain(self, url, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(url))

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_element(self, locator, keys, timeout = 5):
        element = self.wait_visibility(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Проверить, что элемент отображается")
    def is_element_visible(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))
