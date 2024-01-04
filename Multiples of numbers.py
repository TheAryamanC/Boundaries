# There are several ways to implement this

def multiples_lister(until, multiple1, multiple2):
    return sum(i for i in range(until) if (i % multiple1 == 0 or i % multiple2 == 0))

if __name__ == "__main__":
    print("The sum of multiples of 3 and 5 below 1000 is:", multiples_lister(1000, 3, 5))