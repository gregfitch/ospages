"""Home page objects."""
from pypom import Region
from selenium.webdriver.common.by import By

from pages.accounts.base import AccountsBase
from pages.salesforce.home import Salesforce


class Home(AccountsBase):
    """Home page base."""

    @property
    def login(self):
        """Return the login pane."""
        return self.Login(self)

    def log_in(self, user, password):
        """Log into the site with a specific user."""
        return self.Login(self).login(user, password)

    @property
    def logged_in(self):
        """Return user log in status."""
        return self.Login(self).logged_in

    class Login(Region):
        """User login pane."""

        _user_field_locator = (By.ID, 'login_username_or_email')
        _password_field_locator = (By.ID, 'login_password')
        _login_submit_button_locator = (By.CSS_SELECTOR, '.footer > input')
        _password_reset_locator = (By.CSS_SELECTOR, '.footer a')
        _trouble_locator = (By.CSS_SELECTOR, '.trouble')
        _login_help_locator = (By.CSS_SELECTOR, '.login-help')
        _salesforce_link_locator = (By.CSS_SELECTOR, '.login-help a')
        _salesforce_loader = (By.CSS_SELECTOR, 'div.body-and-support-buttons')
        _error_locator = (By.CSS_SELECTOR, '.alert')
        _signup_locator = (By.CSS_SELECTOR, '.extra-info a')

        @property
        def logged_in(self):
            """Return True if a user is logged in."""
            return 'profile' in self.selenium.current_url

        def login(self, user, password):
            """Log into the site with a specific user."""
            self.find_element(*self._user_field_locator).send_keys(user)
            self.find_element(*self._login_submit_button_locator).click()
            self.find_element(*self._password_field_locator) \
                .send_keys(password)
            self.find_element(*self._login_submit_button_locator).click()
            self.wait.until(lambda _: self.logged_in)

        def reset_password(self, user, new_password):
            """Reset a current user's password."""
            self.find_element(*self._password_reset_locator).click()
            assert(False), 'work to be done'

        @property
        def is_help_shown(self):
            """Return True if help text is visible."""
            return self.is_element_displayed(*self._login_help_locator)

        @property
        def toggle_help(self):
            """Show or hide Account help info."""
            self.find_element(*self._trouble_locator).click()
            from time import sleep
            sleep(0.25)
            return self

        def go_to_help(self):
            """Click the Salesforce help link."""
            if not self.is_help_shown:
                self.toggle_help
            current = self.driver.current_window_handle
            self.find_element(*self._salesforce_link_locator).click()
            if current == self.driver.window_handles[0] and \
                    len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[1])
            return Salesforce(self.driver)

        def get_login_error(self):
            """Return Account log in error message."""
            return self.find_element(*self._error_locator).text

        def signup_user(self, email, password, user_type):
            """Sign up as a new user."""
            try:
                from pages.accounts.signup import Signup
            except ImportError:
                # already loaded
                pass
            return Signup(self.driver, email, password, user_type)
