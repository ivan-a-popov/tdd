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
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        
        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda: self.assertEqual(
        self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,  
        "You can't have an empty list item"  
        ))
        
        # User tries again with some text for the item, which now works
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        
        # Perversely, he now decides to submit a second blank list item
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        # He receives a similar warning on the list page
        self.wait_for(lambda: self.assertEqual(
        self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,  
        "You can't have an empty list item"  
        ))

        # And he can correct it by filling some text in
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Make tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

# user1 wonders whether the site will remember his list. Then he sees
# that the site has generated a unique URL for him -- there is some
# explanatory text to that effect.

