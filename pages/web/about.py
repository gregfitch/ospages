"""OpenStax About Us Page."""

from time import sleep

from pypom import Region
from selenium.webdriver.common.by import By

from pages.web.base import WebBase
from utils.utilities import Utility, go_to_
from utils.web import Web


class AboutUs(WebBase):
    """About Us page."""

    URL_TEMPLATE = '/about'

    _root_locator = (By.ID, 'main')
    _image_locators = (By.CSS_SELECTOR, '#main img')
    _who_section_locator = (By.CSS_SELECTOR, 'section.who')
    _what_section_locator = (By.CSS_SELECTOR, 'section.what')
    _where_section_locator = (By.CSS_SELECTOR, 'section.where')
    _map_locator = (By.CLASS_NAME, 'map')

    @property
    def loaded(self):
        """Wait until the three panels are displayed."""
        status = (super().loaded and
                  self.who_we_are.is_displayed() and
                  self.what_we_do.is_displayed() and
                  self.where_were_going.is_displayed())
        return status

    def is_displayed(self):
        """Return True when the About Us page is loaded."""
        return self.loaded

    @property
    def who_we_are(self):
        """Access the Who we are panel."""
        who = self.find_element(*self._who_section_locator)
        return self.WhoWeAre(self, who)

    @property
    def what_we_do(self):
        """Access the What we do panel."""
        what = self.find_element(*self._what_section_locator)
        return self.WhatWeDo(self, what)

    @property
    def where_were_going(self):
        """Access the Where we're going panel."""
        where = self.find_element(*self._where_section_locator)
        return self.WhereWereGoing(self, where)

    @property
    def content_map(self):
        """Return the content map element."""
        return self.find_element(*self._map_locator)

    class WhoWeAre(Region):
        """The Who we are panel."""

        _child_locator = (By.TAG_NAME, 'div')
        _foundation_link_locator = (By.CSS_SELECTOR, '[href$=foundation]')
        _resources_link_locator = (By.CSS_SELECTOR, '[href$=partners]')
        _faq_link_locator = (By.CSS_SELECTOR, '[href$=faq]')

        def is_displayed(self):
            """Return True if the panel is displayed."""
            return self.root.is_displayed()

        def go_to_foundations(self):
            """Follow the philanthropic foundations link."""
            foundations = self.find_element(*self._foundation_link_locator)
            Utility.click_option(self.driver, element=foundations)
            from pages.web.supporters import Supporters
            return go_to_(Supporters(self.driver))

        def go_to_resources(self):
            """Follow the educational resources link."""
            resources = self.find_element(*self._resources_link_locator)
            Utility.click_option(self.driver, element=resources)
            from pages.web.partners import Partners
            return go_to_(Partners(self.driver))

        def go_to_faq(self):
            """Follow the FAQ link."""
            faq = self.find_element(*self._faq_link_locator)
            Utility.click_option(self.driver, element=faq)
            from pages.web.faq import FAQ
            return go_to_(FAQ(self.driver))

    class WhatWeDo(Region):
        """The What we do panel."""

        _library_link_locator = (By.CSS_SELECTOR, '[href$=subjects]')
        _tutor_marketing_link_locator = (By.CSS_SELECTOR, '[href$="-tutor"]')
        _card_locator = (By.CLASS_NAME, 'card')

        def is_displayed(self):
            """Return True if the panel is displayed."""
            return self.root.is_displayed()

        def go_to_library(self):
            """Follow the current library link."""
            library_link = self.find_element(*self._library_link_locator)
            Utility.click_option(self.driver, element=library_link)
            from pages.web.subjects import Subjects
            return go_to_(Subjects(self.driver))

        def go_to_tutor_marketing(self):
            """Follow the OpenStax Tutor Beta link."""
            tutor_link = self.find_element(*self._tutor_marketing_link_locator)
            Utility.click_option(self.driver, element=tutor_link)
            from pages.web.tutor import TutorMarketing
            return go_to_(TutorMarketing(self.driver))

        @property
        def cards(self):
            """Access the cards."""
            return [self.Card(self, element)
                    for element in self.find_elements(*self._card_locator)]

        class Card(Region):
            """An information card."""

            @property
            def image(self):
                """Access the card image."""
                return self.find_element(*self._image_locator)

            def click(self):
                """Click the card."""
                href = self.root.get_attribute('href')
                append = href.split('openstax.org')[-1]
                Utility.click_option(self.driver, element=self.root)
                if Web.SUBJECTS in href:
                    from pages.web.subjects import Subjects as Destination
                elif Web.TUTOR in href:
                    from pages.web.tutor import TutorMarketing as Destination
                elif Web.RESEARCH in href:
                    from pages.web.research import Research as Destination
                elif Web.INSTITUTION in href:
                    from pages.web.partners import Institutional as Destination
                elif Web.PARTNERS in href:
                    from pages.web.partners import Partners as Destination
                elif Web.ROVER in href:
                    from pages.web.rover import Rover as Destination
                else:
                    raise PageNotFound(f'{append} is not a known destination')
                sleep(1.0)
                return go_to_(
                    Destination(self.driver, base_url=self.page.page.base_url))

            @property
            def text(self):
                """Return the card content."""
                return self.find_element(*self._content_locator).text

    class WhereWereGoing(Region):
        """The Where we're going panel."""

        _tutor_marketing_link_locator = (By.LINK_TEXT,
                                         'improving student learning')
        _research_link_locator = (By.CSS_SELECTOR, '[href$=research]')

        def is_displayed(self):
            """Return True if the panel is displayed."""
            return self.root.is_displayed()

        def go_to_student_learning(self):
            """Follow the improving student learning link."""
            learning = self.find_element(*self._tutor_marketing_link_locator)
            Utility.click_option(self.driver, element=learning)
            from pages.web.tutor import TutorMarketing
            return go_to_(
                TutorMarketing(self.driver, base_url=self.page.base_url))

        def go_to_research(self):
            """Follow the research in learning science link."""
            research = self.find_element(*self._research_link_locator)
            Utility.click_option(self.driver, element=research)
            from pages.web.research import Research
            return go_to_(
                Research(self.driver, base_url=self.page.base_url))


class PageNotFound(Exception):
    """Page is not a known destination error."""

    pass
