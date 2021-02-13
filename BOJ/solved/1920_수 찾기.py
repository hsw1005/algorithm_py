# 수 찾기
# 이진탐색

n = int(input())
n_arr = list(map(int, input().split()))

n_arr.sort()

m = int(input())
m_arr = list(map(int, input().split()))

for number in m_arr:
    start = 0
    end = n-1
    answer = 0

    while start <= end:
        mid = (start+end)//2

        if n_arr[mid] == number:
            answer = 1
            break
        elif number < n_arr[mid]:
            end = mid-1
        else:
            start = mid+1
    print(answer)



"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
