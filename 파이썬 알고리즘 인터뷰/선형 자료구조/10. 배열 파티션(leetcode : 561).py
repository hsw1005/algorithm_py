class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
        sum = 0
        pair = []
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum