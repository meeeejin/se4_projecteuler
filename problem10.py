# Project Euler - Problem 10
# Find the sum of all the primes below 2,000,000

prime_list = []

prime_list.append(2)

num = 3
prime_sum = 2
while True:
        for e in prime_list:
                if num % e == 0:
                        break
        if num % e != 0:
                prime_list.append(num)
		prime_sum += num

        num += 2
	if num > 2000000:
		break
	print num

print prime_sum
