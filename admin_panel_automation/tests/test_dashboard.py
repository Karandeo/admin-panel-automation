import pytest
from pages.dashboard_page import DashboardPage

def test_dashboard_header(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open()
    assert dashboard_page.get_dashboard_header() == "Welcome to the Dashboard"
