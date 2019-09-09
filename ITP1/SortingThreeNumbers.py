
def quick_sort(arr, l, r):
    if l < r:
        i = l
        j = r
        pivot = arr[i]
        while i < j:
            while i < j and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i] = arr[j]
                i += 1
            while i < j and arr[i] < pivot:
                i += 1
            if i < j:
                arr[j] = arr[i]
                j -= 1
        arr[i] = pivot
        quick_sort(arr, l, i - 1)
        quick_sort(arr, i + 1, r)


def print_result(arr, n):
    for i in range(n):
        if i > 0:
            print(' ', end='')
        print(arr[i], end='')
    print('\n', end='')


arr = [eval(x) for x in input().split()]
arr.sort()
print_result(arr, arr.__len__())




