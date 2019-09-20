def max_sum_from_start(array):

    array_sum = 0
    max_sum = float("-inf")
    for num in array:
        array_sum += num
        if array_sum > max_sum:
            max_sum = array_sum
    return max_sum


def max_cross_array_sum(array, left, mid, right):

    max_sum_of_left = max_sum_from_start(array[left:mid + 1][::-1])
    max_sum_of_right = max_sum_from_start(array[mid + 1: right + 1])
    return max_sum_of_left + max_sum_of_right


def max_subarray_sum(array, left, right):

    if left == right:
        return array[right]

    mid = (left + right) // 2
    left_half_sum = max_subarray_sum(array, left, mid)
    right_half_sum = max_subarray_sum(array, mid + 1, right)
    cross_sum = max_cross_array_sum(array, left, mid, right)
    return max(left_half_sum, right_half_sum, cross_sum)


n = eval(input())
arr = [eval(x) for x in input().split()]
print(max_subarray_sum(arr, 0, n - 1))
