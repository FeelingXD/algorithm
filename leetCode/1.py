# two-sum
from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            if dic[nums[i]]:
                return sorted([i, dic[nums[i]] - 1])
            dic[target - nums[i]] = i + 1
