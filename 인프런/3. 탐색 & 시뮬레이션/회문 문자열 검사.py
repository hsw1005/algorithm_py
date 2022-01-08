"""
5
level
moon
abcba
soon
gooG
"""

n = int(input())
arr = []
for _ in range(0, n):
    arr.append(input())

for idx, word in enumerate(arr):
    word= word.lower()
    w_arr = list(word)
    left = 0
    right = len(w_arr)-1
    while True:
        if w_arr[left] == w_arr[right]:
            left += 1
            right -= 1
            if left >= right:
                print("#{0} {1}".format(idx+1, "YES"))
                break
        else:
            print("#{0} {1}".format(idx+1, "NO"))
            break