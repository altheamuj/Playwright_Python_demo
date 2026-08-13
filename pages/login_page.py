from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usernameInput = page.get_by_placeholder("Username")
        self.passwordInput = page.get_by_placeholder("Password")
        self.loginButton = page.get_by_role("button", name="Login")
        self.alertMessage = page.get_by_role("alert")
        
        self.forgotPassword = page.get_by_text("Forgot your password?")
        self.cancelButton = page.get_by_role("button", name="Cancel")
        self.resetpasswordButton = page.get_by_role("button", name="Reset Password")

    def login(self, username: str, password: str):
        self.usernameInput.fill(username)
        self.passwordInput.fill(password)
        self.loginButton.click()
        
    def navigate_forgot_password(self):
        self.forgotPassword.click()
        self.page.wait_for_url("**/auth/requestPasswordResetCode")
    
    def submit_reset_password(self, username: str):
        expect(self.usernameInput).to_be_visible
        
        self.usernameInput.fill(username)
        self.resetpasswordButton.click()
        
        self.page.wait_for_url("**/auth/sendPasswordReset")