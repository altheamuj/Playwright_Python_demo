from playwright.sync_api import Page, expect

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page
        self.searchInput = page.get_by_role("textbox", name="Search")

        
    def navigate_and_verify(self, menu_name: str, expected_url: str):
        link = self.page.get_by_role("link", name = menu_name)
        link.click()
        
        expect(self.page).to_have_url(expected_url)
        
        active_link = self.page.locator(f'a.oxd-main-menu-item.active:has-text("{menu_name}")')
        
        expect(active_link).to_be_visible()
        
        
    def search_menu(self, search: str):
        self.searchInput.fill(search)
        self.page.keyboard.press("Enter")
        