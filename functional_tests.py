#!/home/ipopov/dev/PycharmProjects/TDD/bin/python3

from selenium import webdriver
import unittest

class NewUserTest(unittest.TestCase):
    

    def setUp(self):
        self.browser = webdriver.Firefox()
    

    def tearDown(self):
        self.browser.quit()



    def test_start(self):
        '''test: user can start a list and retreive it later'''
        #it generally works -- user gets a start page  
        self.browser.get('http://localhost:8000')
        #user gets the correct start page  
        self.assertIn('To-Do', self. browser.title)
        self.fail('Test finished!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')

# test 3: user is prompted to enter a list element

# test 4: the text 'bla-bla-bla' is entered

# test 5: after pressing enter we refresh the page, and then it contains the element with text 'bla-bla-bla' 

# test 6: there's still a prompt to enter an element

# test 7: user enters text 'abl-abl-abl' and presses enter

# test 8: after page is refreshed, there're two elements on it

# test 9: the unique URL is generated for user

# test 10: user follows the URL, and all two enries are still there

