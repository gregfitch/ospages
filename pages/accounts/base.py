"""Basic page parent for all Accounts pages."""
from pypom import Page, Region
from selenium.webdriver.common.by import By

from pages.rice.home import Rice


class AccountsBase(Page):
    """Base class."""

    _root_locator = (By.CSS_SELECTOR, '.sessions')

    def wait_for_page_to_load(self):
        """Override page load."""
        self.wait.until(
            lambda _: self.find_element(*self._root_locator).is_displayed())

    @property
    def header(self):
        """Return Accounts' header."""
        return self.Header(self)

    @property
    def footer(self):
        """Return Accounts' footer."""
        return self.Footer(self)

    class Header(Region):
        """Accounts header."""

        _root_locator = (By.ID, 'application-header')
        _logo_locator = (By.ID, 'top-nav-logo')

        @property
        def is_header_displayed(self):
            """Header display boolean."""
            return self.loaded

        def go_to_accounts_home(self):
            """Follow the OpenStax icon link back to the site root."""
            self.find_element(*self._logo_locator).click()
            return self

    class Footer(Region):
        """Accounts footer."""

        _root_locator = (By.ID, 'application-footer')
        _rice_link_locator = (By.ID, 'footer-rice-logo')
        _copyright_locator = (By.PARTIAL_LINK_TEXT, 'Copyright')
        _terms_locator = (By.PARTIAL_LINK_TEXT, 'Terms')

        @property
        def is_footer_displayed(self):
            """Footer display boolean."""
            return self.loaded

        @property
        def show_copyright(self):
            """Display the copyright."""
            self.find_element(*self._copyright_locator).click()
            return self

        @property
        def show_terms_of_use(self):
            """Display the terms of use."""
            self.find_element(*self._terms_locator).click()
            return self

        def go_to_rice(self):
            """Load the Rice webpage."""
            self.find_element(*self._rice_link_locator).click()
            return Rice(self.driver)
