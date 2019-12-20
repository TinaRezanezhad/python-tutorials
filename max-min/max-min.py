# algorithm
# get a number from user 
# get number as much as number value 
# set a var for max value 
# set a var for min value 
# set a var for max value
# if i (first step in for) equal to zero so min and max = req_input
# insert continue to prevent to execution of continue the loop
# compare values and put in the variables
# set if and elif for recognition the max and min value
# print min and max value

# string formatting
# list

### Zeinab
number = int(input())
numbers = list()
for i in range (number):
    numbers.append(int(input()))

print("MAX: {0}".format(max(numbers)))
print("MIN: {0}".format(min(numbers)))

### Zeinab





number = int(input())
max = 0
min = 0

for i in range (number):
    req_input = int(input())
    
    if i == 0:
        min = req_input
        max = req_input
        continue

    if req_input > max:
        max = req_input
    elif req_input < min :
        min = req_input
print(max , min)