# Get an integer from user, n, perform the following conditional actions:
# If n is odd, print <n> Is Weird
# If n is even and in the inclusive range of 2 to 5, print <n> Is Not Weird
# If n is even and in the inclusive range 5 of to 20, print <n> Is Weird
# If n is even and greater than 20, print <n> Is Not Weird
# Instead of <n>, you should print the input number.

number = int(input())
remain = number %2 

if 0 <= number <= 5 or number > 20 and remain == 0:
    print(number , " Is Not Weird ")
elif 5 <= number <= 20:
        print(number , "Is Weird")
        