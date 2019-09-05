from array import array

n = eval(input())
arr = array('i')

while n > 0:
    arr.append(eval(input()))
    n -= 1

max_number = arr[1] - arr[0]
min_number = arr[0]
length = len(arr)
for i in range(1, length):
    max_number = max(arr[i] - min_number, max_number)
    min_number = min(arr[i], min_number)

print(max_number)
