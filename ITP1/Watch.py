S = eval(input())

h, m = divmod(S, 3600)
m, s = divmod(m, 60)

print(str(h) + ':' + str(m) + ':' + str(s))

