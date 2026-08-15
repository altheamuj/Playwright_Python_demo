import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture(autouse=True)
def go_to_login(page: Page):
    page.goto("/")
    yield

@pytest.fixture
def logged_in_page(page:Page):
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.wait_for_selector("h6", timeout=10000)
    
    return page