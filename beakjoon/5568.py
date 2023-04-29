# 카드 놓기
import sys
import itertools
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = []
ans = set()
for i in range(n):
    cards.append(int(input()))

for i in itertools.permutations(cards, k):

    ans.add(''.join(map(str, i)))


print(len(ans))
