
while True:
    a, b = input().split()
    a, b = eval(a), eval(b)
    if a == 0 and b == 0:
        break
    if a > b:
        print(str(b) + " " + str(a))
    else:
        print(str(a) + " " + str(b))

