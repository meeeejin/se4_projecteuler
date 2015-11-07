# Project Euler - Problem 7
# Find the 10,001st prime number

prime_list = []

prime_list.append(2)

num = 3
while True:
	for e in prime_list:
		if num % e == 0:
			break
	if num % e != 0:
		prime_list.append(num)
		if len(prime_list) == 10001:
			break
	
	num += 2

print prime_list[10000]
