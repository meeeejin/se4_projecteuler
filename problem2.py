# Project Euler - Problem 2
# Find the sum of the even Fibonacci numbers(<= 4,000,000)

sum = 0
fibo1 = 1
fibo2 = 2
fibo_sum = 0

while fibo1 < 4000000:
	if fibo1 % 2 == 0:
		sum += fibo1
	fibo_sum = fibo1 + fibo2
	fibo1 = fibo2
	fibo2 = fibo_sum

print sum	
