import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class", autouse=True)
def driver(request):

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Параметры для загрузки файлов
    # prefs = {"down.default_directory": f"{os.getcwd()}\download"}
    prefs = {"download.default_directory": os.path.join(os.getcwd(), "download")}
    options.add_experimental_option('prefs', prefs)

    # Создание экземпляра драйвера
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = driver  # Доступ к драйверу в тестовых классах
    yield driver
    driver.quit()