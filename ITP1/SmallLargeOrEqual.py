a, b = input().split()
a, b = eval(a), eval(b)

if a < b:
    print('a < b')
elif a == b:
    print('a == b')
else:
    print('a > b')


