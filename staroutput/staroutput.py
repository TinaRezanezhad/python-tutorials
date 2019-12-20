# 3- Write a program that asks the user for a positive integer
# Do not accept a negative value (or zero) – if the user supplies an invalid value you should
# re-prompt them. Once you have a positive integer you can print that number of stars to the screen. For example:
# Enter a positive integer: -5
# Invalid, try again!
# Enter a positive integer: 0
# Invalid, try again!
# Enter a positive integer: 5
# *****
# Enter a positive integer: +2
# **

number = int(input())

if number < 0:
        print("error: please inter a positive number" )
elif number > 0:
        print("*" * number)
else:
    print( "Invalid, try again!" )
        