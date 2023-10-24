# 옥상정원꾸미기
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    buildings = [int(input()) for _ in range(int(input()))]
    stack = []
    answer = 0
    for b in buildings:
        while stack and stack[-1] <= b:
            stack.pop()
        answer += len(stack)
        stack.append(b)
    print(answer)
    pass
