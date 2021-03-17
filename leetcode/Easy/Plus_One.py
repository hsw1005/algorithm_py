class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = []
        for i in range(0, len(digits)):
            nums.append(str(digits[i]))
        num = "".join(nums)
        num = int(num)
        num += 1
        num = list(str(num))
        return num