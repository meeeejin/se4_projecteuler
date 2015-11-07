# Project Euler - Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers

# Return True if the given number is a palindrome
def isPalindrome(num):
	tmp = 0
	i = num

	while i > tmp:
		tmp = tmp * 10 + i % 10
		i /= 10

	if tmp == i:
		return True
	else:
		return False

if __name__ == '__main__':
	result = 0
	max_result = 0

	for i in range(100, 1000):
		for j in range(i, 1000):
			result = i * j
			if isPalindrome(result) == True:
				if result > max_result:
					max_result = result

	print max_result
