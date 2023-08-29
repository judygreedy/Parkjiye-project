from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient

class BoardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


    def test_board_list(self):
        response = self.client.get('/api/boards/')
        self.assertEqual(response.status_code, 200)


