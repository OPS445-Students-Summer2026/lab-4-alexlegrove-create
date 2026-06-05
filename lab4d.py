#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(word_f5):
    # Place code here - refer to function specifics in section below
    return(str(word_f5[0:5]))

def last_seven(word_l7):
    # Place code here - refer to function specifics in section below
    return(str(word_l7[-7:]))

def middle_number(middle_int):
    # Place code here - refer to function specifics in section below
    middle_num = str(middle_int)
    return(middle_num[1] + middle_num[2])

def first_three_last_three(first_three, last_three):
    # Place code here - refer to function specifics in section below
    return(str(first_three[0:3] + last_three[-3:]))


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))