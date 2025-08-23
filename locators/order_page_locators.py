from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]') # поле имя
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]') # поле фамилия
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # поле адрес
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле Станция метро
    METRO_STATION_LIST = (By.XPATH, '//div[@class="select-search__value"]')
    METRO_OPTIONS = (By.XPATH, "//div[contains(@class,'select-search__select')]//li")
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # поле телефон
    NEXT_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM")]') # кнопка далее
    BUTTON_NEXT = (By.XPATH, "//button[contains(@class,'Button_Button__') and contains(@class,'Button_Middle__') and normalize-space()='Далее']")

    HEADER_ORDER_PAGE =(By.XPATH, '//div[@class="Order_Header__BZXOb"]') # заголовок Про аренду
    DELIVERY_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # поле Когда привезти самокат
    DATEPICKER_OVERLAY = (By.CSS_SELECTOR, ".react-datepicker")
    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[@class="Dropdown-placeholder"]') # поле срок аренды
    RENTAL_OPTIONS = {
        "сутки": (By.XPATH, '//div[contains(@class,"Dropdown-option") and normalize-space()="сутки"]'),
        "двое суток": (By.XPATH, '//div[contains(@class,"Dropdown-option") and normalize-space()="двое суток"]')}
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, '//div[text()="сутки"]') # выбор из списка: сутки
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, '//div[text()="двое суток"]') # выбор из списка: на двое суток
    SCOOTER_BLACK_CHECKBOX = (By.ID, 'black') # чекбокс черного цвета
    SCOOTER_GREY_CHECKBOX = (By.ID, 'grey') # чекбокс серого цвета
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # комментарий для курьера
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and normalize-space()='Заказать']") # кнопка Заказать
    CONFIRM_BUTTON = (By.XPATH, "//button[normalize-space()='Да']") # кнопка подтверждения Да
    HEADER_SUCCESS = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]') # заголовок Заказ оформлен
    SECOND_STEP_HEADER = (By.XPATH, "//*[contains(text(),'Про аренду')]")
    BUTTON_YES = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//*[contains(text(),'Заказ оформлен') or contains(text(),'Номер заказа')]")
    SUCCESS_TEXT = (By.XPATH, "//*[contains(@class,'Order_ModalHeader') or contains(.,'Заказ оформлен')]")