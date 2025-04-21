from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://44.195.125.80:10097/web/dashboard"

    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h1[@class='dashboard-header']")
    
    # Actions
    def open(self):
        self.driver.get(self.url)

    def get_dashboard_header(self):
        return self.driver.find_element(*self.DASHBOARD_HEADER).text
