from django.test import TestCase
from rest_framework.test import APIClient


# Create your tests here.
class TestSampleView(TestCase):
    def test_response_ok(self):
        url = '/api/test/'
        client = APIClient()
        responce = client.get(url)
        self.assertEquals(responce.status_code, 404)
