"""
4
1 2 3 4

"""
"""
1. a[i-1] < a[i]를 만족하는 가장 큰 i를 찾는다.
2. j >= i 이면서, a[j] > a[i-1]을 만족하는 가장 큰 j 를 찾는다. -> 위치가 제일 크면서(j) a[i] 보다 큰 수
3. a[i-1]과 a[j]를 swap한다.
4. a[i]부터 순열을 뒤집는다.
"""

def next_permutation(arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] >= arr[i]: # 1
        i -= 1
    if i <= 0: # 마지막 순열(내림차순 정렬)
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


n = int(input())
arr = list(map(int, input().split()))

if next_permutation(arr):
    print(" ".join(map(str, arr)))
else:
    print(-1)