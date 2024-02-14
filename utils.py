def factorial(n): return 1 if n == 0 else n * factorial(n-1)

def ncd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


def is_palindrome(s):
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    if cleaned_str == cleaned_str[::-1]:
        return True


#for pull-request:
def column_addition(num1, num2, perenis=0):
    if num1 == 0 and num2 == 0 and perenis == 0:
        return ""

    prava_num_1 = num1 % 10
    prava_num_2 = num2 % 10
    current_sum = prava_num_1 + prava_num_2 + perenis
    new_perenis = current_sum // 10
    result_digit = current_sum % 10
    remaining_sum = column_addition(num1 // 10, num2 // 10, new_perenis)

    return str(remaining_sum) + str(result_digit)
