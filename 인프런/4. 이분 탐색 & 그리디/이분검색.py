"""
8 32
23 87 65 12 57 32 99 81
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print(binary_search(arr, m)+1)