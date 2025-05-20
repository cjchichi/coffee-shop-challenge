import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer
from coffee import Coffee
from order import Order
import pytest

class TestCustomer:
    def test_name_validation(self):
        customer = Customer("Alice")
        assert customer.name == "Alice"
        
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
            
    def test_orders(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in customer.orders()
        
    def test_coffees(self):
        customer = Customer("Charlie")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Mocha")
        Order(customer, coffee1, 3.0)
        Order(customer, coffee2, 4.0)
        assert len(customer.coffees()) == 2