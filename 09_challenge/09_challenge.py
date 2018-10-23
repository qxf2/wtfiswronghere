"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""

def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    
    # adding some redundant declarations on purpose
    # we will make our script 'tighter' in one of coming exercises
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 
    min_num = 6

    # Google for 'range in python' to see what it does
    for i in range(min_num,max_num):
        # % or modulo division gives you the remainder 
        if i == min_num:
            print("{} and {} don't have {} , {}".format(num1,num2,three_mul,five_mul))
        elif i%num1==0 and i%num2==0:
            print(i,three_mul+five_mul)
        elif i%num1==0:
            print(i,three_mul)
        elif i%num2==0:
            print(i,five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)