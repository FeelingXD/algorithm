# Next Greater Element I
from collections import defaultdict


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = defaultdict(lambda: -1)
        for v in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[v]:
                ans[nums2[stack.pop()]] = nums2[v]
            stack.append(v)
        ret = list(map(lambda x: ans[x], nums1))
        return ret


# example
Solution().nextGreaterElement([2, 1, 3], [2, 3, 1])
