from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.get_expenses_url = reverse('expenses')

        self.user_data = {
            'email' :'email1@gmail.com',
            'username': 'email1',
            'password' : 'email@gmail.com'
        }

        return super().setUp()


        def tearDown(self):
            return super().tearDown()

