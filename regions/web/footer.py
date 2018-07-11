"""Web's shared footer region."""

from time import sleep

from pypom import Region
from selenium.webdriver.common.by import By


class Footer(Region):
    """OpenStax Web footer region."""

    _root_locator = (By.TAG_NAME, 'footer')

    # Content
    _license_locator = (By.CSS_SELECTOR, "a[href*='license']")
    _terms_of_service_locator = (By.CSS_SELECTOR, "a[href*='tos']")
    _privacy_policy_locator = (By.CSS_SELECTOR, "a[href*='privacy-policy']")
    _accessibility_statement_locator = (
        By.CSS_SELECTOR, "a[href*='accessibility-statement']")
    _open_source_locator = (
        By.CSS_SELECTOR, "a[href*='https://github.com/openstax']")
    _contact_us_locator = (By.CSS_SELECTOR, "a[href*='contact']")
    _press_locator = (By.CSS_SELECTOR, "a[href*='press']")
    _newsletter_locator = (By.PARTIAL_LINK_TEXT, "Newsletter")

    # Social apps
    _facebook_locator = (By.CLASS_NAME, 'facebook')
    _twitter_locator = (By.CLASS_NAME, 'twitter')
    _linkedin_locator = (By.CLASS_NAME, 'linkedin')

    @property
    def is_footer_displayed(self):
        """Return true if the footer is currently displayed."""
        return self.is_displayed

    def go_to_license(self):
        """Go to the website license page."""
        self.find_element(*self._license_locator).click()
        sleep(1)
        from pages.web.license import License
        return License(self.driver)

    def go_to_tos(self):
        """View the terms of service."""
        self.find_element(*self._terms_of_service_locator).click()
        sleep(1)
        from pages.web.terms import Terms
        return Terms(self.driver)

    def go_to_privacy_policy(self):
        """View the privacy policy."""
        self.find_element(*self._privacy_policy_locator).click()
        sleep(1)
        from pages.web.privacy import PrivacyPolicy
        return PrivacyPolicy(self.driver)

    def go_to_accessibility_statement(self):
        """View the accessibility statement."""
        self.find_element(*self._accessibility_statement_locator).click()
        sleep(1)
        from pages.web.accessibility import Accessibility
        return Accessibility(self.driver)

    def go_to_open_source(self):
        """Open GitHub and view the OpenStax repositories."""
        self.find_element(*self._opens_source_locator).click()
        sleep(1)
        from pages.github.home import GitHub
        return GitHub(self.driver)

    def go_to_contact_us(self):
        """Go to the contact form."""
        self.find_element(*self._contact_us_locator).click()
        sleep(1)
        from pages.web.contact import Contact
        return Contact(self.driver)

    def go_to_press(self):
        """View the press page."""
        self.find_element(*self._press_locator).click()
        sleep(1)
        from pages.web.press import Press
        return Press(self.driver)

    def go_to_newsletter(self):
        """Go to the newsletter signup."""
        self.find_element(*self._newsletter_locator).click()
        sleep(1)
        from pages.web.newsletter import NewsletterSignup
        return NewsletterSignup(self.driver)

    def go_to_facebook(self):
        """Go to OpenStax's Facebook page."""
        self.find_element(*self._facebook_locator).click()
        sleep(1)
        from pages.facebook.home import Facebook
        return Facebook(self.driver)

    def go_to_twitter(self):
        """Go to OpenStax's Twitter page."""
        self.find_element(*self._twitter_locator).click()
        sleep(1)
        from pages.twitter.home import Twitter
        return Twitter(self.driver)

    def go_to_linkedin(self):
        """Go to OpenStax's LinkedIn company page."""
        self.find_element(*self._linkedin_locator).click()
        sleep(1)
        from pages.linkedin.home import LinkedIn
        return LinkedIn(self.driver)