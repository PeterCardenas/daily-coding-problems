'''
The area of a circle is defined as pi * r^2. Estimate pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
'''
from random import uniform
from math import pi

def sol():
	num_in_circle = 0
	total = 100000000
	for i in range(total):
		x = uniform(-1, 1)
		y = uniform(-1, 1)
		if x ** 2 + y ** 2 <= 1:
			num_in_circle += 1
	return num_in_circle / total * 4

def main():
	print(f'Real pi: {pi}')
	print(f'Func pi: {sol()}')

main()
