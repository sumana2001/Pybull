"""
Python script to check validity of credit card numbers (using Luhn's algorithm)
Author : https://www.github.com/chatRG
"""

import sys

def usage():
    msg = """
        
        usage:
        python3 CCValidator <credit card number>
        
        example:
        python3 CCValidator 34678253793
        
    """
    print(msg)

def get_cc_number():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    return sys.argv[1]

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

def cc_type(cc_num):
    if 12 <= len(cc_num) and len(cc_num) <= 19:
        print("This is a valid credit card number.")
        if cc_num[0:1] == "4":
            print("Type: Visa card.")
        elif cc_num[0:2] == "34" or cc_num[0:2] == "37":
            print("Type: American Express (AMEX) card.")
        elif cc_num[0:2] == "36":
            print("Type: Diner’s Club International card.")
        elif cc_num[0:2] == "51" or cc_num[0:2] == "52" or cc_num[0:2] == "53" or cc_num[0:2] == "54" or cc_num[0:2] == "55":
            print("Type: Mastercard.")
        elif cc_num[0:4] == "6011":
            print("Type: Discover card.")
    else:
        print("Invalid card number!")

if __name__ == "__main__":
    cc_num = get_cc_number()
    if (validate(cc_num)):
        cc_type(cc_num)
    else:
        print("Invalid card number!")