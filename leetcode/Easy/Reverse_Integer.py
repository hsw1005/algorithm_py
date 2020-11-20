
input = 123
max = 2**31-1
min = -2**31

def reverse(input):
    answer = 0

    if input > 0:
        answer = int(str(input)[::-1])
    elif input < 0:
        answer = -1 * int(str(input*-1)[::-1])

    if input not in range(min, max):
        return 0
    else:
        return answer


    return answer

answer = reverse(input)
print(answer)

'''
result->
Runtime: 32 ms, faster than 58.49% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.4 MB, less than 6.82% of Python3 online submissions for Reverse Integer.
'''