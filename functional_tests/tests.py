#!/home/ipopov/dev/PycharmProjects/TDD/bin/python3

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 5


class NewUserTest(LiveServerTestCase):
    

    def setUp(self):
        self.browser = webdriver.Firefox()
    

    def tearDown(self):
#        self.browser.quit()
        pass


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):
        '''test: user can start a list and retreive it later'''
        
        # the first test: it generally works -- user gets a start page  
        self.browser.get(self.live_server_url)
        
        # user gets the correct start page: the page title and header mention to-do lists  
        self.assertIn('To-Do', self. browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user is prompted to enter a list element
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')    


        # the text 'bla-bla-bla' is entered
        inputbox.send_keys('bla-bla-bla')
        
        # after pressing enter we refresh the page, and then it contains the element with text 'bla-bla-bla' 
        inputbox.send_keys(Keys.ENTER)  
        self.wait_for_row_in_list_table('1: bla-bla-bla')

        # there's still a prompt to enter an element
        inputbox = self.browser.find_element_by_id('id_new_item')

        # user enters text 'abl-abl-abl' and presses enter
        inputbox.send_keys('abl-abl-abl')
        inputbox.send_keys(Keys.ENTER)
        
        # after page is refreshed, there're two elements on it
        self.wait_for_row_in_list_table('1: bla-bla-bla')
        self.wait_for_row_in_list_table('2: abl-abl-abl')


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # test 9: the unique URL is generated for user
        # user starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('bla-bla-bla')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: bla-bla-bla')

        # user  notices that the list has a unique URL
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')

        # Now a new user comes along to the site.

        ## We use a new browser session to make sure that no information
        ##  of user1's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()


        # user2 visits the home page.  There is no sign of user1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('bla-bla-bla', page_text)
        self.assertNotIn('abl-abl-abl', page_text)

        # user2 starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Kill Bill')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Kill Bill')

        # user2 gets his own unique URL
        user2_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(user2_list_url, user1_list_url)

        # Again, there is no trace of user1's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('bla-bla-bla', page_text)
        self.assertIn('Kill Bill', page_text)


# test 10: user follows the URL, and all two enries are still there

