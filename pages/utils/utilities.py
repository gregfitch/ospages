"""Helper functions for OpenStax Pages."""

from random import randint
from time import sleep

from faker import Faker
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import Select


class Utility(object):
    """Helper functions for various Pages functions."""

    HEX_DIGITS = '0123456789ABCDEF'

    @classmethod
    def select(cls, driver, element_locator, label):
        """Select an Option from a menu."""
        return Utility.fast_multiselect(driver, element_locator, [label])

    @classmethod
    def fast_multiselect(cls, driver, element_locator, labels):
        """Select menu multiselect options.

        Daniel Abel multiselect
        'https://sqa.stackexchange.com/questions/1355/
        what-is-the-correct-way-to-select-an-option-using-seleniums-
        python-webdriver#answer-2258'
        """
        select = Select(driver.find_element(*element_locator))
        for label in labels:
            select.select_by_visible_text(label)
        return select

    @classmethod
    def selected_option(cls, driver, element_locator):
        """Return the currently selected option."""
        return Select(driver.find_element(*element_locator)) \
            .first_selected_option \
            .text

    @classmethod
    def scroll_to(cls, driver, element_locator):
        """Scroll the screen to the element found at the locator."""
        driver.execute_script('arguments[0].scrollIntoView();',
                              driver.find_element(*element_locator))

    @classmethod
    def random_hex(cls, length=20):
        """Return a random hex number of size length."""
        return ''.join([Utility.HEX_DIGITS[randint(0, 0xF)]
                       for _ in range(length)])

    @classmethod
    def random(cls, start=0, end=100000):
        """Return a random integer from start to end."""
        return randint(start, end)

    @classmethod
    def random_name(cls, is_male=None, is_female=None):
        """Generate a random name list for Accounts users."""
        fake = Faker()
        name = ['', '', '', '']
        if is_female:
            use_male_functions = False
        elif is_male:
            use_male_functions = True
        else:
            use_male_functions = randint(0, 2) == 0
        has_prefix = randint(0, 10) >= 6
        has_suffix = randint(0, 10) >= 8

        if has_prefix:
            name[0] = fake.prefix_male() if use_male_functions else \
                fake.prefix_female()
        name[1] = fake.first_name_male() if use_male_functions else \
            fake.first_name_female()
        name[2] = fake.last_name()
        if has_suffix:
            name[3] = fake.suffix_male() if use_male_functions else \
                fake.suffix_female()
        return name

    @classmethod
    def random_phone(cls, area_code=713, number_only=True):
        """Return a random phone number."""
        template = ('{area}5550{local}' if number_only else
                    '({area}) 555-0{local}')
        return template.format(area=area_code, local=randint(100, 199))

    @classmethod
    def fake_email(cls, first_name, surname, id=False):
        """Return a name-based fake email."""
        template = ('{first}.{second}.{random}@os.fake.org')
        return template.format(first=first_name,
                               second=surname,
                               random=id if id else Utility.random(100, 999))

    @classmethod
    def new_tab(cls, driver):
        """Open another browser tab."""
        driver.execute_script('window.open();')
        sleep(1)
        return driver.window_handles

    @classmethod
    def switch_to(cls, driver, link_locator):
        """Switch to the other window handle."""
        current = driver.current_window_handle
        driver.find_element(*link_locator).click()
        sleep(1)
        new_handle = 1 if current == driver.window_handles[0] else 0
        if len(driver.window_handles) > 1:
            driver.switch_to.window(
                driver.window_handles[new_handle])

    @classmethod
    def compare_colors(cls, left, right):
        """Return True if two RGB color strings match."""
        return Color.from_string(left) == Color.from_string(right)

    @classmethod
    def get_test_credit_card(cls, card=None, status=None):
        """Return a random card number and CVV for test transactions."""
        braintree = Card()
        _card = card if card else Status.VISA
        _status = status if status else Status.VALID
        test_cards = braintree.get_by(Status.STATUS, _status)
        test_cards = braintree.get_by(Status.TYPE, _card, test_cards)
        select = randint(0, len(test_cards) - 1)
        use_card = test_cards[select]
        return (use_card['number'], use_card['cvv'])


class Card(object):
    """Fake card objects."""

    def __init__(self):
        """Retrieve card numbers from BTP."""
        import requests
        from bs4 import BeautifulSoup

        braintree = (
            'https://developers.braintreepayments.com/'
            'reference/general/testing/python'
        )
        section_list_selector = 'table:nth-of-type({position}) tbody tr'
        response = requests.get(braintree)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        resp = BeautifulSoup(response.text, 'html.parser')
        self.options = []

        for card_status in range(Status.VALID, Status.OTHER + 1):
            for card in resp.select(
                    section_list_selector.format(position=card_status)):
                fields = card.select('td')
                card_processor = (Status.VISA
                                  if fields[0].text[0] == '4'
                                  else fields[1].text)
                if card_processor == Status.AMEX:
                    cvv = '{:04}'.format(randint(0, 9999))
                else:
                    cvv = '{:03}'.format(randint(0, 999))
                rest = fields[2].text if len(fields) > 2 else ''
                data = fields[1].text if card_status == Status.OTHER or  \
                    card_status == Status.TYPED else ''
                self.options.append({
                    'number': fields[0].text,
                    'cvv': cvv,
                    'type': card_processor,
                    'status': card_status,
                    'response': rest,
                    'data': data,
                })

    def get_by(self, field=None, state=None, use_list=None):
        """Return a subset of test cards with a specific type."""
        _field = field if field else Status.STATUS
        _state = state if state else Status.VALID
        _use_list = use_list if use_list else self.options
        return list(
            filter(
                lambda card: card[_field] == _state,
                _use_list
            )
        )


class Status(object):
    """Card states."""

    STATUS = 'status'
    VALID = 2
    NO_VERIFY = 3
    TYPED = 4
    OTHER = 5

    TYPE = 'type'
    AMEX = 'American Express'
    DINERS = 'Diners Club'
    DISCOVER = 'Discover'
    JCB = 'JCB'
    MAESTRO = 'Maestro'
    MC = 'Mastercard'
    VISA = 'Visa'

    RESPONSE = 'response'
    DECLINED = 'processor declined'
    FAILED = 'failed (3000)'
