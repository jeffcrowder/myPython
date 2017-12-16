from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle

c = Car(12304, 'ford', 'fiesta', 1999, None)
t = Truck(150000, 'chevy', 'tahoe', 2003, None)
m = Motorcycle(4000, 'honda', 'whatever', 2009, None)

print('Car:')
print(c.vehicle_type())
print(c.sale_price())
print(c.base_sale_price)
print(c.purchase_price())

print('Truck')
print(t.vehicle_type())

print('Motorcycle')
print(m.vehicle_type())


