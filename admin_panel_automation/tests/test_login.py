import pytest
from pages.login_page import LoginPage
from utils.config import Config

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    assert driver.current_url == "http://44.195.125.80:10097/web/dashboard"

def test_login_failure(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)
    assert "Invalid credentials" in login_page.get_error_message()
