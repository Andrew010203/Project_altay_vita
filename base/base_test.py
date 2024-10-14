import pytest

from config.data import Data
from pages.reg_page import RegPage


class BaseTest:

    data: Data

    reg_page: RegPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.reg_page = RegPage(driver)
