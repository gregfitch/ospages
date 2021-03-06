"""The OpenStax Instagram landing page."""

from pypom import Page
from selenium.webdriver.common.by import By


class Instagram(Page):
    """The OpenStax Instagram page."""

    URL_TEMPLATE = 'https://www.instagram.com/openstax/'

    _username_locator = (By.CSS_SELECTOR, 'h1')

    @property
    def loaded(self):
        """Return True if the username is found."""
        return bool(self.find_element(*self._username_locator))

    def is_displayed(self):
        """Return True if the main content is loaded."""
        return 'openstax' in self.driver.page_source

    @property
    def location(self):
        """Return the current URL."""
        return self.driver.current_url
