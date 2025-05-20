import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer
from order import Order
import pytest

class TestCoffee:
    def test_name_validation(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")
            
    def test_name_immutability(self):
        coffee = Coffee("Espresso")
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
            
    def test_orders(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Alice")
        order = Order(customer, coffee, 5.0)
        assert order in coffee.orders()
        
    def test_customers(self):
        coffee = Coffee("Americano")
        customer1 = Customer("Bob")
        customer2 = Customer("Charlie")
        Order(customer1, coffee, 4.0)
        Order(customer2, coffee, 4.5)
        assert len(coffee.customers()) == 2