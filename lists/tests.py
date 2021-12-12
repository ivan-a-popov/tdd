from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):
 
 
   def test_home_page(self):
        '''test: home page returns correct html'''
        response = self.client.get('/')
        html = response.content.decode('utf8')  
        # new test checks if the correct template was rendered
        self.assertTemplateUsed(response, 'home.html')
