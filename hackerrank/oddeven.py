# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n = int(input())
result = n % 2


if result == 0 and 6 <= n <= 20 or result != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird ")
else:
    print("Not Weird")
