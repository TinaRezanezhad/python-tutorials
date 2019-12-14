# algorithm
#
# 1. get a number from user
# 2. divide the number by two
# 3. if the quotient of the division doesn't equals to 1 print denominator and go to step 2
# 4. otherwise print quotient
# 5. Exit


# code

number= int(input())
result = ''

while number != 0:
    result = result + str(number % 2)
    number = int(number / 2)


print(result[::-1])



# trace and debug

# given 4
# expect 100
# number = 4
# while 2 != 1 
# print 0



