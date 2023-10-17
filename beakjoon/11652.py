# 카드
from math import inf
import sys
from collections import defaultdict
input = sys.stdin.readline
if __name__ == "__main__":
    card = defaultdict(int)
    for _ in range(int(input())):
        card[n := int(input())] += 1
    print(sorted(card.items(), key=lambda x: (-x[1], x[0]))[0][0])
