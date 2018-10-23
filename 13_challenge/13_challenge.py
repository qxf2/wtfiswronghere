"Add typo in a method name"


def fizzbuzz(self,max_num):
    "This method implements FizzBuzz"
    print('fizzbuzz')
    # adding some redundant declarations on purpose
    # we will make our script 'tighter' in one of coming exercises
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 

    # Google for 'range in python' to see what it does
    for i in range(1,max_num):
        # % or modulo division gives you the remainder 
        if i%num1==0 and i%num2==0:
            print(i,three_mul+five_mul)
        elif i%num1=0:
            print(i,three_mul)
        elif i%num2==0:
            print(i,five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)