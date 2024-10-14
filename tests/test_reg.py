import time
import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Buy product")
class TestCriticalPath(BaseTest):

    @allure.title("Check search and buy product")
    @allure.severity("Critical")
    # @pytest.mark.smoke
    # @pytest.mark.run(order=1)
    def test_critical_path(self):
        self.reg_page.open()
        self.reg_page.is_opened()
        self.reg_page.check_main_word()
        self.reg_page.enter_personal_account()
        self.reg_page.input_login(self.data.LOGIN)
        self.reg_page.enter_login_button()
        self.reg_page.input_password(self.data.PASSWORD)
        self.reg_page.input_search_field()
        self.reg_page.choose_product()
        self.reg_page.add_to_cart()
        self.reg_page.go_to_cart()
        self.reg_page.click_place_an_order_button()
        self.reg_page.check_order()
        self.reg_page.go_to_checkout()
        self.reg_page.click_dalee_button()
        self.reg_page.input_phone()
        self.reg_page.click_dalee_button()
        self.reg_page.input_city()
        self.reg_page.click_dalee_button()
        self.reg_page.click_good_button()
        self.reg_page.click_dalee_button()
        self.reg_page.choose_delivery_method()
        self.reg_page.input_address()
        self.reg_page.scroll_page(0, 750)
        self.reg_page.input_fio()
        self.reg_page.input_email_field()
        self.reg_page.click_oform_button()
        self.reg_page.click_good_button()
        self.reg_page.click_oform_button()
        self.reg_page.make_screenshot("order placed")


