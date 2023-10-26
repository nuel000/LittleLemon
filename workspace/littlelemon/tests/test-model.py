from django.test import TestCase
from LittleLemonAPI.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        expected_result = "IceCream : 80"
        self.assertEqual(item.get_item(), expected_result)
