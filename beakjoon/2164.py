# 카드2
from collections import deque

cards = deque([i for i in range(1, (int(input())+1))])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards.pop())
