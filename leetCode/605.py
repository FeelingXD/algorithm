# Can Place Flowers

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        lf = len(flowerbed)
        prv = 0
        for i in range(lf):
            nxt = 0 if i == lf-1 else flowerbed[i+1]
            if prv == 0 and nxt == 0 and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
            prv = flowerbed[i]
            if n == 0:
                return True
        return False
