from collections import deque


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        word1 = deque(word1)
        word2 = deque(word2)
        while word1 and word2:
            answer.append(word1.popleft())
            answer.append(word2.popleft())
        if word1 or word2:
            if word1:
                answer = answer+list(word1)
            else:
                answer = answer+list(word2)
        return ''.join(answer)
