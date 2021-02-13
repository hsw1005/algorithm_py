
while True:
    arr = list(map(int, input().split()))
    arr.sort()

    if arr[0] == 0 & arr[1] == 0 & arr[2] == 0:
        break
    else:
        if arr[0]*arr[0] + arr[1]*arr[1] == arr[2]*arr[2]:
            print("right")
        else:
            print("wrong")


"""
6 8 10
25 52 60
5 12 13
0 0 0
"""