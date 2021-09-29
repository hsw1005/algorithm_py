arr = ['a', 'a', 'b', 'c', 'c']

arr2 = list(set(arr))

dictionary = {item: 0 for item in arr2}
answer = []

for i in range(0, len(arr)):
    if arr[i] in dictionary.keys():
        dictionary[arr[i]] += 1

for i in dictionary:
    pass

print(answer)