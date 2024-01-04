def num_to_list(number):
    return [int(i) for i in list(str(number))]

def is_palindrome(list_of_digits):
    length = len(list_of_digits)
    is_Palindrome = False
    if length == 5:
        if (list_of_digits[0] == list_of_digits[4]) and (list_of_digits[1] == list_of_digits[3]):
            is_Palindrome = True
    if length == 6:
        if (list_of_digits[0] == list_of_digits[5]) and (list_of_digits[1] == list_of_digits[4]) and (list_of_digits[2] == list_of_digits[3]):
            is_Palindrome = True
    return is_Palindrome

if __name__ == "__main__":
    max_palindrome = 0
    for i in range(100, 999):
        for j in range(100, 999):
            num = i * j
            list_num = num_to_list(num)
            if is_palindrome(list_num) and num > max_palindrome:
                max_palindrome = num

    print(max_palindrome)