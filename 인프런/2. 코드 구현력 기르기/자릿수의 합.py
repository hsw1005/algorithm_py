def digit_sum(x):
    sum_num = [int(i) for i in str(x)]

    return sum(sum_num)

n = int(input())

arr = list(map(int, input().split()))

store = []

for i in arr:
    store.append(digit_sum(i))

where = store.index(max(store))

print(arr[where])