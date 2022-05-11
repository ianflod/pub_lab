import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Perceval Smith", 15, 100.00)
        self.pub = Pub("The Steves Head", 100.00)

    def test_customer_name(self):
        self.assertEqual("Perceval Smith", self.customer.name)

    def test_customer_wallet(self):
        self. assertEqual(100, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(15, self.customer.age)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(5)
        self.assertEqual(95, self.customer.wallet)

    def test_increase_drunkenness(self):
        self.customer.increase_drunkenness(5)
        self.assertEqual(5, self.customer.drunkenness)

# the ultimate test
    def test_customer_buys_drink(self):
        drink1 = Drink("Beer", 5.95, 5)
        
        self.pub.increase_till(drink1.price)
        self.customer.decrease_wallet(drink1.price)
        self.customer.increase_drunkenness(drink1.alcohol)
        self.assertEqual(105.95, self.pub.till) 
        self.assertEqual(94.05, self.customer.wallet) 
        self.assertEqual(5, self.customer.drunkenness)




