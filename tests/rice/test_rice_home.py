"""Rice model stub."""

from pages.rice.home import Rice
from tests.markers import nondestructive, test_case


@test_case('C195133')
@nondestructive
def test_at_rice(base_url, selenium):
    """Return True if at Rice's webpage."""
    page = Rice(selenium, base_url).open()
    assert(page.at_rice), 'Not at the Rice University homepage'
