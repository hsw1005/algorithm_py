x = -101
def isPalindrome(x):
    answer = False
    temp = str(x)[::-1]

    if(temp == str(x)):
        answer = True
    else:
        pass
    max = 2*31-1
    min = -2*31-1

    if answer not in range(min, max):
        return 0
    else:
        return answer

answer = isPalindrome(x)
print(answer)

'''
result ->
Runtime: 64 ms, faster than 50.82% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 43.57% of Python3 online submissions for Palindrome Number.
'''