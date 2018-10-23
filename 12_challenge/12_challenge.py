"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""
class FizzBuzz():

    def __init__(self):
        "Initializer"
        # adding some redundant declarations on purpose
        # we will make our script 'tighter' in one of coming exercises
        self.num1 = 3
        self.num2 = 4
        self.three_mul = 'fizz'
        self.five_mul = 'buzz'

    
    def fizzbuzz(self,max_num):
        "This method implements FizzBuzz"

        # Google for 'range in python' to see what it does
        for i in range(1,max_num):
            # % or modulo division gives you the remainder 
            if i%self.num1==0 and i%self.num2==0:
                print(i,self.three_mul+self.five_mul)
            elif i%self.num1==0:
                print(i,self.three_mul)
            elif i%self.num2==0:
                print(i,self.five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    #Testing the fizzbuzz class
    test_obj = FizzBuzz()
    test_obj.fizzbuzz(100)
