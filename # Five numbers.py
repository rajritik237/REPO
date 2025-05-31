# Five numbers
a = 12
b = 45
c = 7
d = 33
e = 29

# Using if-elif-else ladder to find the greatest number
if a >= b and a >= c and a >= d and a >= e:
    print("a is the greatest:", a)
elif b >= a and b >= c and b >= d and b >= e:
    print("b is the greatest:", b)
elif c >= a and c >= b and c >= d and c >= e:
    print("c is the greatest:", c)
elif d >= a and d >= b and d >= c and d >= e:
    print("d is the greatest:", d)
else:
    print("e is the greatest:", e)
