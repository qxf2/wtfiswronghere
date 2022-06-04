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
    three_multiple = 'fizz'
    five_multiple = 'buzz'
    number_three = 3
    number_five = 5 

    # Google for 'range in python' to see what it does
    for value in range(1,max_num):
        # % or modulo division gives you the remainder 
        if value%number_three==0 and value%number_five==0:
            print(value,three_multiple+five_multiple)
        elif value%number_three==0:
            print(value,three_multiple)
        elif value%number_five==0:
            print(value,five_multiple)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)
