"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""

def fizzbuzz():
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 
    for i in range(1, max_num):
        if i % num1 == 0 and i % num2 == 0:
            print(i,three_mul+five_mul)
        elif i % num1 == 0:
            print(i,three_mul)
        elif i % num2 == 0:
            print(i,five_mul)
    
if __name__=='__main__':
    fizzbuzz(100)