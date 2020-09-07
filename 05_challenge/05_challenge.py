"""
We will use this script to teach Python to absolute beginners
The script is an example of reading the numbers from file in Python

The problem is: 
For all integers between 1 and 99 (include both):
    # Read the input 3,5 and 99 from the input file
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
    with open('myfile.txt','r') as f:
        print('i have created')
        num1 = int(f.readline())   
        num2=int(f.readline())        
        max_num = int(f.readline())
         
    # Google for 'range in python' to see what it does
    for i in range(1,max_num):
        # % or modulo division gives you the remainder 
        if i%num1==0 and i%num2==0:
            print(i,three_mul+five_mul)
        elif i%num1==0:
            print(i,three_mul)
        elif i%num2==0:
            print(i,five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)
