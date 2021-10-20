nums = []
target = 0
answer = []


# 1. brute force
def twoSum1(nums, target):

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


'''
results ->

Runtime: 548 ms, faster than 28.38% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Two Sum.
'''


# 2. in
# 타겟에서 첫번째 값을 뺀 target - n 이 존재하는지.

def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)


# 3. 투포인터 (투포인터는 정렬된 상태에서만 적용이 가능하다.)
def twoSum3(nums, target):

    left, right = 0, len(nums) - 1

    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return nums[left], nums[right]

answer = twoSum1([7, 11, 2, 15], 9)
print(answer)

left, right = twoSum3([2, 7, 11, 15], 9)
print(left, right)