# 저작권
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    A, I = map(int, input().split())
    print(A*(I-1)+1)
    pass
