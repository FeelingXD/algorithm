# 효율적인 화폐 구성
# 첫줄에 갯수와 target이 주어짐


n, target = map(int, input().split())
coins = list(map(int, input().split()))
INF = 10001
dp = [INF]*INF
dp[0] = 0
for coin in coins:
    dp[coin] = 1
for coin in coins:
    for j in range(coin, INF):
        if dp[j-coin] != INF:
            dp[j] = min(dp[j], dp[j-coin]+1)
if dp[target] == INF:
    print(-1)
else:
    print(dp[target])
