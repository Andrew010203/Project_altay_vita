import allure

from base.base_page import BasePage
from config.links import Links

from selenium.webdriver.support import expected_conditions as EC


class RegPage(BasePage):
    PAGE_URL = Links.MAIN_PAGE

    MAIN_WORD = ("xpath", '//span[text()="Личный кабинет "]')
    LOGIN_FIELD = ("xpath", '(//input[@name="aj_login"])[1]')
    LOGIN_BUTTON = ("xpath", '(//button[@class="main-btn green sign-in"])[1]')
    PASSWORD_FIELD = ("xpath", '//input[@name="password"]')
    SUBMIT_BUTTON = ("xpath", '(//button[@type="submit"])[3]')

    SEARCH_FIELD = ("xpath", '//input[@placeholder="Поиск товаров"]')
    PRODUCT = ("xpath", '//a[@href="/ru/product/rejshi-kaps/"]')

    CART_BUTTON = ("xpath", '(//button[@class="main-btn blue"])[1]')
    CART = ("xpath", '(//a[@href="/cart/"])[1]')
    PRODUCT_PRICE = ("xpath", '(//span[@class="dropdown-total font-medium"])[1]')
    PRICE_IN_CART = ("xpath", '(//span[@class="dropdown-offer-total font-medium js-total"])[1]')
    PLACE_AN_ORDER_BUTTON = ("xpath", '(//a[@class="dropdown-offer-btn main-btn green link-blue"])[1]')
    PRICE_CART = ("xpath", '//span[@class="js-total_products_amount"]')
    TOTAL_COST = ("xpath", '(//span[@class="js-cart_page_total_amount"])[1]')
    GO_TO_CHECKOUT = ("xpath", '(//input[@value="Перейти к оформлению"])[1]')
    DALEE_BUTTON = ("xpath", '//button[text()="Далее"]')
    CITY_FIELD = ("xpath", '//input[@id="shipping_city-input"]')

    PHONE_FIELD = ("xpath", '//input[@id = "auth_phone_email"]')

    CHOOSE_CITY = ("xpath", '//div[text()="Архангельская обл, Архангельск"]')
    GOOD_BUTTON = ("xpath", '//button[text()="Хорошо"]')
    POST_BUTTON = ("xpath", '//label[@for="input-shipping-russian_post"]')
    ADDRESS_FIELD = ("xpath", '//input[@id="shipping_type_russian_post_address"]')
    FIO_FIELD = ("xpath", '//input[@id="shipping_fio_ru"]')
    EMAIL_FIELD = ("xpath", '//input[@id="shipping_email"]')
    PLACE_AN_ORDER_BTN = ("xpath", '(//button[text()="Оформить заказ"])[1]')

    @allure.step("Проверка заголовка страницы")
    def check_main_word(self):
        self.wait.until(EC.text_to_be_present_in_element(self.MAIN_WORD, 'Личный кабинет')), "Текст не совпадает"

    @allure.step("Вход в персональный аккаунт")
    def enter_personal_account(self):
        self.wait.until(EC.element_to_be_clickable(self.MAIN_WORD)).click()

    @allure.step("Ввод логин")
    def input_login(self, LOGIN):
        field = self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD))
        field.clear()
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD)).send_keys(LOGIN)

    @allure.step("Клик на кнопку войти")
    def enter_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    @allure.step("Ввод пароля")
    def input_password(self, PASSWORD):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(PASSWORD)

    @allure.step("Ввод в стороку поиска название товара")
    def enter_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Ввод в стороку поиска название товара")
    def input_search_field(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD)).send_keys("гриб рейши")
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD)).click()

    @allure.step("Выбор товара из списка")
    def choose_product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT)).click()

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()

    @allure.step("Вход в корзину, сравнение стоимости товара с итоговой ценой")
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART)).click()
        product_price = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_PRICE)).text
        print(product_price)
        price_in_cart = self.wait.until(EC.visibility_of_element_located(self.PRICE_IN_CART)).text
        print(price_in_cart)
        assert product_price == price_in_cart, "Цена не совпадает"

    @allure.step("Клик по кнопке Оформить заказ")
    def click_place_an_order_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_AN_ORDER_BUTTON)).click()

    @allure.step("Предварительная проверка заказа")
    def check_order(self):
        product_price = self.wait.until(EC.visibility_of_element_located(self.PRICE_CART)).text
        print(product_price)
        total_cost = self.wait.until(EC.visibility_of_element_located(self.TOTAL_COST)).text
        print(total_cost)
        assert product_price == total_cost, "Цена не совпадает"

    @allure.step("Перейти к оформлению")
    def go_to_checkout(self):
        self.wait.until(EC.visibility_of_element_located(self.GO_TO_CHECKOUT)).click()

    @allure.step("Клик на кнопку далее")
    def click_dalee_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DALEE_BUTTON)).click()

    @allure.step("Ввод номера телефона")
    def input_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).send_keys("+79990000000")

    @allure.step("Ввод названия города доставки")
    def input_city(self):
        self.wait.until(EC.element_to_be_clickable(self.CITY_FIELD)).send_keys("Архангельск")
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_CITY)).click()

    @allure.step("Клик на кнопку Хорошо")
    def click_good_button(self):
        self.wait.until(EC.element_to_be_clickable(self.GOOD_BUTTON)).click()

    @allure.step("Выбор способа доставки")
    def choose_delivery_method(self):
        self.wait.until(EC.element_to_be_clickable(self.POST_BUTTON)).click()

    @allure.step("Ввод адреса")
    def input_address(self):
        self.wait.until(EC.element_to_be_clickable(self.ADDRESS_FIELD)).send_keys("Ленина 20")

    @allure.step("Ввод фамилия имя отчество")
    def input_fio(self):
        self.wait.until(EC.element_to_be_clickable(self.FIO_FIELD)).send_keys("Иванов Иван Иваныч")

    @allure.step("Ввод email")
    def input_email_field(self):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys("puk.kak.03@mail.ru")

    @allure.step("Клик на кнопку Оформить")
    def click_oform_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_AN_ORDER_BTN)).click()
