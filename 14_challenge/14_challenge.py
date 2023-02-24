def fibonacci_fizzbuzz(n):
    a, b = 0, 1
    for i in range(n):
        if a % 3 == 0 and a % 5 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
        a, b = b, a+b
        # Example usage: print the first 20 Fibonacci numbers with FizzBuzz
fibonacci_fizzbuzz(20)