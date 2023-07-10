from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = gcd(len(str1), len(str2))
        answer = ""
        for i in range(min_len+1):
            print(str1[:i])
            if str1.replace(str1[:i], "") == "" and str2.replace(str1[:i], "") == "":
                answer = str1[:i]
        return answer

    @classmethod
    def getDivisor(self, n: int):
        divisorsList = []
        for i in range(1, int(n**1/2)+1):
            if (n % i == 0):
                divisorsList.append(i)
                if ((i**2) != n):
                    divisorsList.append(n//i)
        divisorsList.sort()
        return divisorsList
