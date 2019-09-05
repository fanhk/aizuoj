a, b, c = input().split()
a, b, c = eval(a), eval(b), eval(c)

if a < b < c:
    print("Yes")
else:
    print("No")
