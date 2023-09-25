# 파도반 수열
import sys
input = sys.stdin.readline
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]


def padoban(n):
    global dp
    if n <= len(dp)-1:
        return dp[n]
    else:
        for _ in range(n+1-len(dp)):
            dp.append(dp[-1]+dp[-5])
        return dp[-1]


if __name__ == "__main__":
    for _ in range(T := int(input())):
        print(padoban(int(input())))
