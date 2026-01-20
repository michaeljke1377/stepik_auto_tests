import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.qa-practice.com/elements/button/simple"

class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "req_header")

    @pytest.mark.smoke
    @pytest.mark.win10
    @pytest.mark.skip
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "submit-id-submit")

    @pytest.mark.xfail
    def test_guest_should_see_password_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "password")

