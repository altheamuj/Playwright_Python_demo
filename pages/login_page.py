from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usernameInput = page.get_by_placeholder("Username")
        self.passwordInput = page.get_by_placeholder("Password")
        self.loginButton = page.get_by_role("button", name="Login")
        self.alertMessage = page.get_by_role("alert")
        
    def login(self, username: str, password: str):
        self.usernameInput.fill(username)
        self.passwordInput.fill(password)
        self.loginButton.click()