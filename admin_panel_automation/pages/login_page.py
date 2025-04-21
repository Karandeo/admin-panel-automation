from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://44.195.125.80:10097/web/login"

    # Locators
    USERNAME_INPUT = (By.ID, "vd@yopmail.com")
    PASSWORD_INPUT = (By.ID, "Qwerty@123")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message']")

    # Actions
    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
