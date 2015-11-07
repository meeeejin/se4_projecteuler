# Project Euler - Problem 5
# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

check_list = [11, 12, 13, 14, 16, 17, 18, 19, 20]

# the product of the prime numbers(2,3,5,7,9,11,13,17,19)
num = 9699690

while True:
	finished = False
	for i in check_list:
		if num % i != 0:
			break
		elif num % i == 0 and i == 20:
			finished = True

	if finished == True:
		break

	num += 1
print num
