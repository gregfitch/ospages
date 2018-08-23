"""OpenStax payment home page object."""

from selenium.webdriver.common.by import By

from pages.payments.base import PaymentsBase
from pages.payments.email_logs import EmailLogs
from pages.payments.orders import PaymentOrders
from regions.payments.nav import PaymentsNav
from regions.payments.section import PaymentsListSection


class PaymentsHome(PaymentsBase):
    """OpenStax payment home page object."""

    _section_locator = (By.CSS_SELECTOR, '#content-main div')

    @property
    def nav(self):
        """Return the nav bar region."""
        return PaymentsNav(self)

    @property
    def sections(self):
        """Return a list of section objects."""
        return [PaymentsListSection(self, element)
                for element in self.find_elements(*self._section_locator)]

    def go_to_section(self, idx):
        """Scroll to section with the input index."""
        section = self.find_elements(*self._section_locator)[idx]
        self.driver.execute_script('arguments[0].scrollIntoView();', section)
        return PaymentsListSection(self, section)

    def go_to_orders(self):
        """Go to the orders page."""
        self.go_to_section(3).items[1].click_item()
        return PaymentOrders(self.driver)

    def go_to_email_logs(self):
        """Go to the orders page."""
        self.sections[2].items[0].click_item()
        return EmailLogs(self.driver)