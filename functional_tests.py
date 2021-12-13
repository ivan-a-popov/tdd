#!/home/ipopov/dev/PycharmProjects/TDD/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewUserTest(unittest.TestCase):
    

    def setUp(self):
        self.browser = webdriver.Firefox()
    

    def tearDown(self):
#        self.browser.quit()
        pass


    def test_start(self):
        '''test: user can start a list and retreive it later'''
        
        #it generally works -- user gets a start page  
        self.browser.get('http://localhost:8000')
        
        #user gets the correct start page: the page title and header mention to-do lists  
        self.assertIn('To-Do', self. browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #user is prompted to enter a list element
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')    


        #the text 'bla-bla-bla' is entered
        inputbox.send_keys('bla-bla-bla')
        
        #after pressing enter we refresh the page, and then it contains the element with text 'bla-bla-bla' 
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1) 
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertIn('1: bla-bla-bla', [row.text for row in rows]) 

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')


# test 6: there's still a prompt to enter an element

# test 7: user enters text 'abl-abl-abl' and presses enter

# test 8: after page is refreshed, there're two elements on it

# test 9: the unique URL is generated for user

# test 10: user follows the URL, and all two enries are still there

