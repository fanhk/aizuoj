def max_subarray_sum(array, n):

    this_sum = 0
    max_sum = -1
    start, end, temp = 0, 0, 0
    for i in range(n):
        this_sum += array[i]
        if this_sum > max_sum:
            max_sum = this_sum
            end = i
            start = temp
        elif this_sum < 0:
            this_sum = 0
            temp = i + 1

    return max_sum, start, end


n = eval(input())
arr = [eval(x) for x in input().split()]
result = max_subarray_sum(arr, n)
# print(arr)
# print(n)
# print(arr[n-1])
if result[0] >= 0:
    print(result[0], arr[result[1]], arr[result[2]], sep=' ')
else:
    print(0, arr[0], arr[n - 1], sep=' ')
