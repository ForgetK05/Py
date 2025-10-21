import math
value = input()

def check_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

flag = None

if value.isdigit():
    value = int(value)
    flag = "INTEGER"
    check_odd_even = None
    check_prime_value = None 
    
    if value % 2 == 0:
        check_odd_even = "EVEN"
    else:
        check_odd_even = "ODD"

    if check_prime(value):
        check_prime_value = "PRIME"
    else:
        check_prime_value = "NOT PRIME"


    print(f"{flag} {check_odd_even} {check_prime_value}")

else:
    if "." in value:
        phan_nguyen, phan_thuc = value.split(".") # 2.5 -> [2, 5]
        value = float(value)
        
        flag = "FLOAT"

        check_neg_pos = None

        if value > 0:
            check_neg_pos = "POSITIVE"
        elif value < 0:
            check_neg_pos = "NEGATIVE"
        else:
            check_neg_pos = "ZERO"

        print(f"{flag} {check_neg_pos}")

    else:
        print(f"STRING {'PALINDROME' if value == value[::-1] else 'NOT PALINDROME'} LENGTH: {value.__len__()}")