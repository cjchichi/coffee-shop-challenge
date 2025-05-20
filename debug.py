from customer import Customer
from coffee import Coffee
from order import Order

customer1 = Customer("Elvis")
customer2 = Customer("Mercy")
customer3 = Customer("Alvin")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")
coffee3 = Coffee("Cappuccino")

order1 = Order(customer1, coffee1, 5.0)
order2 = Order(customer1, coffee2, 3.5)
order3 = Order(customer2, coffee1, 4.0)
order4 = Order(customer2, coffee3, 6.0)
order5 = Order(customer3, coffee1, 5.5)
order6 = Order(customer3, coffee1, 4.5)

print("Customer 1 orders:", [o.coffee.name for o in customer1.orders()])
print("Coffee 1 orders count:", coffee1.num_orders())
print("Coffee 1 average price:", coffee1.average_price())
print("Customers who ordered Latte:", [c.name for c in coffee1.customers()])
print("Top Latte customer:", Customer.most_aficionado(coffee1).name)