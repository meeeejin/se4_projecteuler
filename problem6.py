# Project Euler - Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sum_of_squares = 0
for i in range(1, 101):
	sum_of_squares += i * i

sum = 0
for i in range(1, 101):
	sum += i

square_of_sum = sum * sum

print abs(sum_of_squares - square_of_sum)
