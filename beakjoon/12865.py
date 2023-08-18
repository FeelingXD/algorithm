# 평범한 배낭
import sys
input = sys.stdin.readline

# 물품수 N 무게 K
N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
wl = [0]
vl = [0]

for _ in range(N):
    w, v = map(int, input().split())
    wl.append(w)
    vl.append(v)


for r in range(1, N+1):
    for c in range(1, K+1):
        if c < wl[r]:
            dp[r][c] = dp[r-1][c]
        else:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-wl[r]]+vl[r])
print(dp[N][K])
