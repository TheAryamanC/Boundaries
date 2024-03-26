import time

# The Fibonacci sequence is quite a famous sequence
# It is generated using the previous two numbers in the sequence
# The first two numbers are typically 0 and 1, although they can be any two numbers to generate a sequence (which is not the Fibonacci sequence but shares the same properties)
# The sequence is typically defined as F(n) = F(n-1) + F(n-2) where F(0) = 0 and F(1) = 1

# Computers easily generate the Fibonacci sequence
# The sequence is used in many algorithms and is a good example of recursion
# Here is a simple recursive function to generate the nth Fibonacci number
def fibonacci(n):
    if n == 0 or n == 1:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# We can make this function slighly more tidy using a one-liner
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 0
    
# The problem with this function is that it is very slow
# To get an estimate of how slow, let us try to generate the 30th and 35th Fibonacci number

if __name__ == "__main__":
    start = time.time()
    print("Fib(30) with recursion", fibonacci(30))
    print("Time taken:", time.time() - start)

    start = time.time()
    print("Fib(35) with recursion", fibonacci(35))
    print("Time taken:", time.time() - start)

# The time taken is quite long - it typically takes about 1 second to generate the 30th Fibonacci number and 13 seconds to generate the 35th Fibonacci number
# And this is just the beginning - the time taken grows exponentially with the number - generating the 40th Fibonacci number would take several minutes this way
# Why? Well, the function is calling itself multiple times for the same number, which leads to a lot of repeated calculations
# This is a classic example of a problem that can be solved using dynamic programming
# However, I will not touch on that paradigm in this snippet
# All that is relevant is that we can use the general formula to generate the sequence by building up the sequence from the first two numbers
# This is much faster than the recursive approach
    
def fibonacci(n):
    terms = [0] * n
    terms[0] = 0 # technically redundant, but it is good to be explicit
    terms[1] = 1
    for i in range(2, n):
        terms[i] = terms[i - 1] + terms[i - 2]
    return terms[n-1]

if __name__ == "__main__":
    start = time.time()
    print("Fib(30) with storing data", fibonacci(30))
    print("Time taken:", time.time() - start)

    start = time.time()
    print("Fib(35) with recursion", fibonacci(35))
    print("Time taken:", time.time() - start)

# Now, we have a much faster function - it takes virtually no time to generate either number
# We can talk about time complexity, but that is not the point of this snippet
# The point is that we now have a very fast way to generate the Fibonacci sequence
# Now let us play around and see what we can find out
    
# The first thing I want to mention is that the Fibonacci sequence is closely related to the golden ratio
# The golden ratio is a number that is approximately 1.61803398875 - it is seen in many places in nature and is considered to be aesthetically pleasing
# Although it is possible to mathematically show, I will not prove anything here, merely show that it appears in the Fibonacci sequence
# So let us see how the Fibonacci sequence relates to the golden ratio
def return_fibonacci(n):
    terms = [0] * n
    terms[0] = 0
    terms[1] = 1
    for i in range(2, n):
        terms[i] = terms[i - 1] + terms[i - 2]
    return terms

def golden_ratio(n):
    sequence = return_fibonacci(n)
    return float(sequence[n - 1] / sequence[n - 2]), float(sequence[n - 2] / sequence[n - 1])

if __name__ == "__main__":
    print(golden_ratio(1000))