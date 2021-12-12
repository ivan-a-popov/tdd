from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
 

    def test_root_url(self):
        '''test: root url '/' resolves to home page view'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
