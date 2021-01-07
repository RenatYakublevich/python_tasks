from collections import namedtuple


Car = namedtuple('Car', 
				['color',
				'speed'])

my_car = Car('red',150)
print(my_car.speed)