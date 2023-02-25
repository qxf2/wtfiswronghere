"""
We will use this script to teach Python to absolute beginners
The script is an example of  is an implementation of the FizzBuzz problem

The problem is:
"""

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = input("Enter a number: ")
fizzbuzz(n)

