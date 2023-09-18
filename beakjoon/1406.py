# 에디터
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    word = list(map(str, input().strip()))
    sub_stack = []
    c = len(word)
    for _ in range(int(input())):
        cmd = input().split()
        match cmd:
            case ["L"]:
                sub_stack.append(word.pop()) if word else None
            case ["D"]:
                word.append(sub_stack.pop()) if sub_stack else None
            case ["B"]:
                word.pop() if word else None
            case "P", v:
                word.append(v)
    print(''.join(list(word)+list(sub_stack)[::-1]))
