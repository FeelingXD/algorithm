# Contains Duplicate
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        return any(num in check or check.add(num) for num in nums)
