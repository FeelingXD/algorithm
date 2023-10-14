# 서로 다른 부분 문자열의 개수
import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().strip()
    answer = set()
    for i in range(len(word)):
        for j in range(i, len(word)):
            answer.add(word[i:j+1])
    print(len(answer))
