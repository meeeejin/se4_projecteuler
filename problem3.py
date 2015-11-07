# Project Euler - Problem 3
# Find the largest prime factor of the number 600851475143

num = 600851475143
p = 2
max_p = 0

while num != 1:
	if num % p == 0:
		num /= p
		if max_p <= p:
			max_p = p
		p = 2
	else:
		p += 1

print max_p

