import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from customer import Customer
from coffee import Coffee
import pytest

class TestOrder:
    def test_initialization(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order.price == 5.0
        
    def test_price_validation(self):
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        with pytest.raises(TypeError):
            Order(customer, coffee, "5")
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.5)
            
    def test_price_immutability(self):
        customer = Customer("Charlie")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 5.0)
        with pytest.raises(AttributeError):
            order.price = 6.0