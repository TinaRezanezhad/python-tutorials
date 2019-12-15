# algorithm
#
# 1. get "number" from user
# 2. let "result" hold my final bits - it is initialized by an empty string
# 3. while number > 0:
#        result = result + remaining of (number / 2)
#        number = number / 2
# 4. output the reverse of the "result"

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



