def generate_fibonacci_numbers(until):
    terms = [0, 1]
    x1 = 0
    x2 = 1
    while x1 + x2 <= until:
        terms.append(x1 + x2)
        x1, x2 = x2, x1 + x2
    return terms

#golden ratio pops up here
def consequtive_quotients(until):
    sequence = generate_fibonacci_numbers(until)
    return [float(sequence[len(sequence) - 1] / sequence[len(sequence) - 2]), float(sequence[len(sequence) - 2] / sequence[len(sequence) - 1])]

if __name__ == "__main__":
    print(generate_fibonacci_numbers(1000))
    print(consequtive_quotients(1000))

    less_than_4_m = generate_fibonacci_numbers(4000000)
    total_even_less_4_m = 0
    for term in less_than_4_m:
        if term % 2 == 0:
            total_even_less_4_m += term
    print(total_even_less_4_m)