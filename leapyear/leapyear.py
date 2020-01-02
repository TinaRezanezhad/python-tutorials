def is_leap(year):
    l1 = year % 4
    l2 = year % 400
    l3 = year % 100
    if l1 == 0 and (l2 == 0 or l3 != 0):
        return True
    else:
        return False

year = int(input())