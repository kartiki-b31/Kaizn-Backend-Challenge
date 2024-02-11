from django.test import TestCase
from django.urls import reverse
from restApi.models import Items
from restApi.serializer import ItemSerializer


class ItemsViewTestCase(TestCase):
    def setUp(self):
        # Create some test data for the Items model
        self.item1 = Items.objects.create(name='Item 1', price=10)
        self.item2 = Items.objects.create(name='Item 2', price=20)

    def test_get_items(self):
        # Test the GET request to retrieve all items
        url = reverse('items-api')
        response = self.client.get(url)
        
        # Verify that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Verify that the response data contains the serialized items
        expected_data = ItemSerializer([self.item1, self.item2], many=True).data
        self.assertEqual(response.json(), expected_data)

    def test_unauthenticated_access(self):
        # Test accessing the endpoint without authentication
        url = reverse('items-api')
        response = self.client.get(url)
        
        # Verify that the response status code is 401 Unauthorized
        self.assertEqual(response.status_code, 401)
