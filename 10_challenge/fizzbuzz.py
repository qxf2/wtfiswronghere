def fizzbuzz(max_num):
    "This method implements FizzBuzz"
    # Google for 'range in python' to see what it does
    for i in range(1,max_num):
        # % or modulo division gives you the remainder 
        if i%3==0 and i%5==0:
            print(i,"fizzbuzz")
        elif i%3==0:
            print(i,"fizz")
        elif i%5==0:
            print(i,"Buzz")