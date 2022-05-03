#!/home/ipopov/dev/PycharmProjects/TDD/bin/python3

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to the home page and accidentally tries to submit
        # an empty list item. He hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        # The browser intercepts the request, and does not load the
        # list page
        self.wait_for(lambda: self.browser.find_element(By.CSS_SELECTOR, '#id_text:invalid'))
        
        # User tries again with some text for the item, and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element(By.CSS_SELECTOR, '#id_text:valid'))
        
        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        # Perversely, he now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for(lambda: self.browser.find_element(By.CSS_SELECTOR, '#id_text:invalid'))

        # And he can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element(By.CSS_SELECTOR, '#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

# user1 wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some
# explanatory text to that effect.

