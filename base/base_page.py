import datetime
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 20, poll_frequency=1)

    """Метод открытия страницы ресурса"""
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    """Проверка открылась ли страница ресурса"""
    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    """Метод создания скриншота"""
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    """Scroll"""
    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
        print("scroll to element")

    """Метод взаимодействия со слайдером"""
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.release()
        action.perform()
        return (x_coords, y_coords)

    def drag_and_drop(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.release()
        action.perform()


