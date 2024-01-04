def prime(num):
    is_prime = True
    range_to = num // 2
    for i in range(2, range_to+1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

if __name__ == "__main__":
    primes = []
    num = 2
    while len(primes) != 10001:
        if prime(num):
            primes.append(num)
        num += 1
    print(primes[10000])