# 단어 정렬
import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in "&"*n:
    words.append(input().strip())
words = list(set(words))
words.sort(key=lambda x: (len(x)))

for word in words:
    print(word)
