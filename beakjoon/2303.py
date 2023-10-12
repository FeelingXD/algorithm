# 숫자 게임
import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    values = []
    answer = []

    for i in range(int(input())):
        values.append(list(map(int, input().split())))
    for i, value in enumerate(values, 1):
        tmp = 0
        for c in combinations(value, 3):
            if tmp < sum(c) % 10:
                tmp = sum(c) % 10
        answer.append(tmp)
    peak = max(answer)
    print(answer.index(peak)+1 if answer.count(peak) ==
          1 else len(answer) - answer[::-1].index(peak))
