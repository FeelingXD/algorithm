# 키로거
import sys
from collections import deque
input = sys.stdin.readline


def solution(word):
    ls, rs = deque(), deque()
    for c in word:
        match c:
            case '>':
                if rs:
                    ls.append(rs.popleft())
                pass
            case '<':
                if ls:
                    rs.appendleft(ls.pop())
                pass
            case '-':
                if ls:
                    ls.pop()
                pass
            case c:
                ls.append(c)
    print(''.join(ls+rs))
    pass


if __name__ == "__main__":
    for _ in range(case := int(input())):
        solution(input().strip())
    pass
