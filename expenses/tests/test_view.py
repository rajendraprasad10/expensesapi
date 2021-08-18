from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from ..models import User
from authentication.tests.test_views import TestView

class TestView1(TestView):
    
    def test_get_expenses_data(self):
        res = self.client.get(self.get_expenses_url, format='json')
        print(res.data)
        self.assertEqual(res.status_code, 200)