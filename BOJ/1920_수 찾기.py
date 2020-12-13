# 수 찾기

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if m_arr[j] == n_arr[i]:
            print('1')
            continue
        else:
            print('0')
            break

print(n_arr)
print(m_arr)


"""
5
4 1 5 2 3
5
1 3 7 9 5
"""