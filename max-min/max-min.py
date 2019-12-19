# algorithm
# get a number from user 
# get number as much as number value 
# set a var for max value 
# set a var for min value 
# set a var for max value 
# compare values with each other


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