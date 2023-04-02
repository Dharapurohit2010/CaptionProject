import pytest
from selenium import webdriver


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("http://tutorialsninja.com/demo/")
        yield
        self.driver.quit()