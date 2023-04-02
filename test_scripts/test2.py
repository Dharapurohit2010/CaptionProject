from lib2to3.pgen2 import driver

import pytest
from base.browser import WebDriverWrapper
from selenium.webdriver import Keys


class TestLoginUI(WebDriverWrapper):
    def test_homepage_title(self):
        self.driver.get("http://tutorialsninja.com/demo/index.php")
        assert "Your Store" in self.driver.title

    def test_search_functionality(self):
        self.driver.get("http://tutorialsninja.com/demo/index.php")
        search_box = self.driver.find_element_by_name("search")
        search_box.clear()
        search_box.send_keys("MacBook")
        search_box.send_keys(Keys.RETURN)
        assert "Search - MacBook" in self.driver.title
        assert self.driver.find_element_by_css_selector(".product-layout")

    def test_add_to_cart(self):
        self.driver.get("http://tutorialsninja.com/demo/index.php")
        search_box = self.driver.find_element_by_name("search")
        search_box.clear()
        search_box.send_keys("iPhone")
        search_box.send_keys(Keys.RETURN)
        add_to_cart_button = self.driver.find_element_by_css_selector("button[data-original-title='Add to Cart']")
        add_to_cart_button.click()
        assert "Shopping Cart" in browser.title
        assert self.driver.find_element_by_css_selector(".table-responsive")

    def test_register_user(self):
        self.driver.get("http://tutorialsninja.com/demo/index.php")
        my_account_link = self.driver.find_element_by_css_selector("a[title='My Account']")
        my_account_link.click()
        register_link = self.driver.find_element_by_link_text("Register")
        register_link.click()
        firstname_input = self.driver.find_element_by_name("firstname")
        firstname_input.send_keys("alex")
        lastname_input = self.driver.find_element_by_name("lastname")
        lastname_input.send_keys("bira")
        email_input = self.driver.find_element_by_name("email")
        email_input.send_keys("alexbira@gmail.com")
        telephone_input = self.driver.find_element_by_name("telephone")
        telephone_input.send_keys("1234567890")
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys("Passw@rd")
        confirm_input = self.driver.find_element_by_name("confirm")
        confirm_input.send_keys("Passw@rd")
        agree_checkbox = self.driver.find_element_by_name("agree")
        agree_checkbox.click()
        continue_button = self.driver.find_element_by_css_selector("input[type='submit'][value='Continue']")
        continue_button.click()
        assert "Your Account Has Been Created!" in self.driver.title

