x, y = map(int, input().split())
day = 0

if x == 1:
    day += y
elif x == 2:
    day += 31 + y
elif x == 3:
    day += 59 + y
elif x == 4:
    day += 90 + y
elif x == 5:
    day += 120 + y
elif x == 6:
    day += 151 + y
elif x == 7:
    day += 181 + y
elif x == 8:
    day += 212 + y
elif x == 9:
    day += 243 + y
elif x == 10:
    day += 273 + y
elif x == 11:
    day += 304 + y
elif x == 12:
    day += 334 + y

if day % 7 == 0:
    print("SUN")
elif day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
