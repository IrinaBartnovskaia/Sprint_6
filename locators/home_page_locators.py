from selenium.webdriver.common.by import By


class HomePageLocators(object):
    ORDER_BUTTON_UP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']") # верхняя кнопка Заказать
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]") # нижняя кнопка Заказать

    LOGO_YANDEX_LINK = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI") # логотип Яндекс
    LOGO_SCOOTER_LINK = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR") # логотип Самокат
    COOKIE_CLOSE_BUTTON =(By.ID, "rcc-confirm-button") # кнопка Да все привыкли(закрыть куки)

    # "Вопросы о важном" (вопросы)
    FAQ_QUESTIONS = {
        0: (By.ID, "accordion__heading-0"),
        1: (By.ID, "accordion__heading-1"),
        2: (By.ID, "accordion__heading-2"),
        3: (By.ID, "accordion__heading-3"),
        4: (By.ID, "accordion__heading-4"),
        5: (By.ID, "accordion__heading-5"),
        6: (By.ID, "accordion__heading-6"),
        7: (By.ID, "accordion__heading-7"),
    }

    FAQ_ANSWERS = {
        0: (By.ID, "accordion__panel-0"),
        1: (By.ID, "accordion__panel-1"),
        2: (By.ID, "accordion__panel-2"),
        3: (By.ID, "accordion__panel-3"),
        4: (By.ID, "accordion__panel-4"),
        5: (By.ID, "accordion__panel-5"),
        6: (By.ID, "accordion__panel-6"),
        7: (By.ID, "accordion__panel-7"),
    }