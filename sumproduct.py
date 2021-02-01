num = int(input('Enter an integer: '))
choose = input('Choose to find the sum or the product of the integers starting from 1 preceding and including the integer you chose:  ')
if choose == "sum".lower():
	sum = 0
	for num in range(n+1):
		sum += num
	print(sum)
if choose == "product".lower() or "factorial".lower():
	product = 1
	for num in range (1, num + 1):
		product *= num
	print(product)