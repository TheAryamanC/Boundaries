import math
import time

def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime

def prime_factors(number):
    primes = []
    for i in range(2, int(math.sqrt(number))):
        if (number % i == 0) and prime(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    print(prime_factors(600851475143))
    print(max(prime_factors(600851475143)))