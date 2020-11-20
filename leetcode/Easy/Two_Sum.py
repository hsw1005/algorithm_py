nums = []
target = 0
answer = []

def twoSum(nums, target):

    for i in range(0, len(nums)):
        for j in range(0, i):
            if not i == j:
                if nums[i]+nums[j] == target:
                    answer.append(j)
                    answer.append(i)
                    break
                else:
                    continue
            else:
                continue

    return answer

answer = twoSum([3, 2, 4], 6)
print(answer)

'''
results ->

Runtime: 548 ms, faster than 28.38% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Two Sum.
'''