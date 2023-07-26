# Reverse Vowels of a String (문자열 모음 뒤집기)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        spells = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        answer = []
        for c in s:
            if c in vowels:
                spells.append(c)
        for c in s:
            if c in vowels:
                answer.append(spells.pop())
            else:
                answer.append(c)
        return ''.join(answer)
