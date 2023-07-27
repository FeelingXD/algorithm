# is Subsequence 부분집합 확인
from collections import defaultdict


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = 0

        if len(s) == 0:
            return True

        for v in t:
            if v == s[cnt]:
                cnt += 1
            if cnt == len(s):
                return True
        return False
