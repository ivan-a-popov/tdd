#!/home/ipopov/dev/PycharmProjects/TDD/bin/python3

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):
        # User goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # User tries again with some text for the item, which now works

        # Perversely, he now decides to submit a second blank list item

        # He receives a similar warning on the list page

        # And he can correct it by filling some text in
        self.fail('write me!')

# user1 wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some
# explanatory text to that effect.

