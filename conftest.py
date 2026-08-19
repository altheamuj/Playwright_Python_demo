import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture(autouse=True)
def go_to_login(page: Page):
    page.goto("/")
    yield

@pytest.fixture
def logged_in_page(page:Page):
    login_page = LoginPage(page)
    username = os.environ["ADMIN_USERNAME"]
    password = os.environ["ADMIN_PASSWORD"]
    login_page.login(username, password)
    
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    page.wait_for_selector("h6", timeout=10000)
    
    return page