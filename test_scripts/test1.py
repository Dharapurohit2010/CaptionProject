import time
import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.web_listener import WebDriverWrapper


class TestAddNewUser(WebDriverWrapper):
    @pytest.mark.parametrize('useremail,userpassword,expected_error',data_source.test_invalid_login_data)
    def test_invalid_login(self,useremail,userpassword,expected_error):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Login')]").click()
        self.driver.find_element(By.NAME,'email').send_keys("johnsina@gmail.com")
        self.driver.find_element(By.NAME,'password').send_keys("Passw@rd1")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        #verify error_message by java script

        actual_error = self.driver.find_element_by_css_selector(".alert-danger")
        assert_that(actual_error).contains(expected_error)

    def test_valid_login(self,useremail,userpassword):
        @pytest.mark.parametrize('useremail,userpassword')
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Login')]").click()
        self.driver.find_element(By.NAME, 'email').send_keys("johnsina@gmail.com")
        self.driver.find_element(By.NAME, 'password').send_keys("Passw@rd")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()


