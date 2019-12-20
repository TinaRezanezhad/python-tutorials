# algorithm
# 1. input from users 
# 2. input as much as first input 
# 3. compare inputs 
# 4. print biggest input 

number = int(input())
max_input = 0
for i in range (number):
    req_input = int(input())
    if req_input > max_input:
        max_input = req_input
    else:
        req_input < max_input 
print(max_input)

