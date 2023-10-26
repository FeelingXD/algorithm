# 나는 친구가 적다(small)

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().strip()
    target = input().strip()
    chracters = []
    for c in word:
        if not c.isdigit():
            chracters.append(c)
    print(answer := 1 if target in ''.join(chracters) else 0)

    pass
