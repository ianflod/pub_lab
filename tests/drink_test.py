import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Beer", 5.95 , 5)
        self.drink2 = Drink("Rum", 10.75, 15)
        self.drink3 = Drink("Whiskey", 15.25, 20)

    def test_drink_name(self):
         self.assertEqual("Whiskey", self.drink3.name)

    def test_drink_price(self):
        self.assertEqual(10.75, self.drink2.price)