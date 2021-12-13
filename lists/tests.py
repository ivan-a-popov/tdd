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


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

