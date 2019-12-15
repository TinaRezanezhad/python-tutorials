number = int(input())
counter = 0
for i in range (1 , number+1):
    result = number % i
    if result == 0:
        counter = counter + 1

if counter == 2:
    print('is prime')
else:
    print('not prime')

