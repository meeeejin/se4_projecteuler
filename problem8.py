# Project Euler - Problem 8
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product and the value of this product

num_series_str = []

num_series_str.append("73167176531330624919225119674426574742355349194934")
num_series_str.append("96983520312774506326239578318016984801869478851843")
num_series_str.append("85861560789112949495459501737958331952853208805511")
num_series_str.append("12540698747158523863050715693290963295227443043557")
num_series_str.append("66896648950445244523161731856403098711121722383113")
num_series_str.append("62229893423380308135336276614282806444486645238749")
num_series_str.append("30358907296290491560440772390713810515859307960866")
num_series_str.append("70172427121883998797908792274921901699720888093776")
num_series_str.append("65727333001053367881220235421809751254540594752243")
num_series_str.append("52584907711670556013604839586446706324415722155397")
num_series_str.append("53697817977846174064955149290862569321978468622482")
num_series_str.append("83972241375657056057490261407972968652414535100474")
num_series_str.append("82166370484403199890008895243450658541227588666881")
num_series_str.append("16427171479924442928230863465674813919123162824586")
num_series_str.append("17866458359124566529476545682848912883142607690042")
num_series_str.append("24219022671055626321111109370544217506941658960408")
num_series_str.append("07198403850962455444362981230987879927244284909188")
num_series_str.append("84580156166097919133875499200524063689912560717606")
num_series_str.append("05886116467109405077541002256983155200055935729725")
num_series_str.append("71636269561882670428252483600823257530420752963450")

product = 0
max_product = 0
num_series = []

for s in num_series_str:
	for c in s:
		num_series.append(c)

for i in range(0, len(num_series)-4):
	product = int(num_series[i]) * int(num_series[i+1]) * int(num_series[i+2]) * int(num_series[i+3]) * int(num_series[i+4])
	if product > max_product:
		max_product = product

print max_product	
