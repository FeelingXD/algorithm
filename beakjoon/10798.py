# 세로 읽기
import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    words = []
    for _ in range(5):
        words.append(f'{input().strip():15}')
    for y in range(15):
        for x in range(5):
            if words[x][y] == " ":
                continue
            print(words[x][y], end="")
