# Project Euler - Problem 9
# Find the product of Pythagorean triplet a, b, c which a + b + c = 1000

finished = False
for i in range(1, 1000, 1):
	for j in range(1, 1000-i, 1):
		k = 1000 - i - j
		if i ** 2 + j ** 2 == k ** 2:
			finished = True
			break
	if finished == True:
		break

print i*j*k
