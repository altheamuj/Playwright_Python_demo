import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.login
def test_successful_login(logged_in_page: Page):
    expect(logged_in_page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(logged_in_page.get_by_role("heading", name="Dashboard")).to_be_visible()
    
@pytest.mark.login
def test_failed_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("test_user", "test123")
    
    expect(login_page.alertMessage).to_be_visible()
    expect(login_page.alertMessage).to_have_text("Invalid credentials")

@pytest.mark.forgot_password
def test_forgot_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_forgot_password()
    login_page.submit_reset_password("test_user")
    
    expect(page.get_by_text("Reset Password link sent successfully")).to_be_visible()

@pytest.mark.forgot_password
def test_cancel_forgot_password(page: Page):
    login_page = LoginPage(page)
    login_page.navigate_forgot_password()
    login_page.cancelButton.click()
    
    page.wait_for_url("**/auth/login")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()