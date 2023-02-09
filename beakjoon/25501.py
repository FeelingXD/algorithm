# 재귀의 귀재
import sys
input = sys.stdin.readline
case = int(input())


def recur(s, l, r, c):
    if l >= r:
        return (1, c)
    elif s[l] != s[r]:
        return (0, c)
    else:
        return recur(s, l+1, r-1, c+1)


def isPelindrom(s):
    return recur(s, 0, len(s)-1, 1)


for _ in range(case):
    value = input().strip()
    isPelindrom(value)
    print(f'{isPelindrom(value)[0]} {isPelindrom(value)[1]}')
