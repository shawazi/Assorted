def fib(number):
    n = 0
    fibseq = [1, 1]
    while n < number - 2:
        fibseq.append(fibseq[-1] + fibseq[-2])
        n += 1
    print(fibseq)

fib(100)
print('Use the fib function to find any number of entries for the fibonnaci sequence')
