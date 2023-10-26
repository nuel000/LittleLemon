from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Dates Pie",price=15.99,inventory = 5)
        Menu.objects.create(title="Sushi Roll",price=33.99,inventory = 20)
        
    def test_getall(self):
        menu_objects = Menu.objects.all()
        serialized_data = [
            {
                'name': menu.title,
                'price': menu.price,
                'inventory':menu.inventory
            }
            for menu in menu_objects
        ]
        
        url = reverse('menu-list')
        response = self.client.get(url)
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        serialized_data = MenuSerializer(Menu.objects.all(), many=True).data
        self.assertEqual(response.data, serialized_data)
        print(serialized_data)

        