from pages.base_page import BasePage


class AuthPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    INVALID_USER_ERROR_BLOCK = "h3[data-test='error']:has-text('Username and password do not match')"
    EMPTY_USER_ERROR_BLOCK = "h3[data-test='error']:has-text('Username is required')"
    BANNED_USER_ERROR_BLOCK = "h3[data-test='error']:has-text('this user has been locked out')"

    def authorize(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)