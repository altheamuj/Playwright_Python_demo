from playwright.sync_api import Page, expect
from pages.navigation_page import NavigationPage

def test_navigate_to_admin (logged_in_page: Page):
    expect(logged_in_page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(logged_in_page.get_by_role("heading", name="Dashboard")).to_be_visible()
    
    navigate_page = NavigationPage(logged_in_page)
    navigate_page.navigate_and_verify("Admin", "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    expect(logged_in_page.get_by_role("heading", name="Admin")).to_be_visible()
    

def test_navigate_to_pim (logged_in_page: Page):
    expect(logged_in_page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(logged_in_page.get_by_role("heading", name="Dashboard")).to_be_visible()
    
    navigate_page = NavigationPage(logged_in_page)
    navigate_page.navigate_and_verify("PIM", "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    expect(logged_in_page.get_by_role("heading", name="PIM")).to_be_visible()

