def max_subarray_sum(array, n):

    this_sum = max_sum = 0
    for i in range(n):
        this_sum += array[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


n = eval(input())
arr = [eval(x) for x in input().split()]
print(max_subarray_sum(arr, n))
