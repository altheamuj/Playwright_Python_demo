from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page:Page):
    login_page = LoginPage(page)
    
    page.goto("/")
    
    login_page.login("Admin", "admin123")
    
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    
def test_failed_login(page:Page):
    login_page = LoginPage(page)
    
    page.goto("/")
    
    login_page.login("test_user", "test123")
    
    expect(login_page.alertMessage).to_be_visible()
    expect(login_page.alertMessage).to_have_text("Invalid credentials")