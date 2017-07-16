"""

Given an integer n, find out total possible bit string (either 0 or 1) of length n which don't have two contiguous zeroes in them.

For this problem statement, the total possible bit string is directly depended on the fibonacci series of the given integer n.
So by using the fibonacci series, we can get the required solution.

"""

def fibonacci_series(n):
    if not(1 <= n <= pow(10,15)):
        print("Length of Bit String is not in the given range")

    num1 = num2 = 1

    while (n > 0):
        result = ( num1 + num2 ) % (pow(10,9)+7)    #Have added the modulo here to reduce the processing time
        num2 = num1
        num1 = result 
        n = n - 1

    print(result)


t = int(input(""))
bit_length = []

if not(1 <= t <= pow(10,3)):
    print("Number of test cases is not in the given range")

else:
    for index in range(t):
        bit_length.append(int(input("")))
        
    for index in range(t):
        fibonacci_series(bit_length[index])

