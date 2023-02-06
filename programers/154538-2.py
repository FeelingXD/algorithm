# 숫자 변환하기 dp
def solution(x, y, n):
    if x >= y:
        return 0
    dp = [float('inf') for i in range(y+1)]
    dp[x] = 0
    for i in range(x, y+1):
        if dp[i] == float('inf'):
            continue
        if i*3 <= y:
            dp[i*3] = min(dp[i*3], dp[i]+1)
        if i*2 <= y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i+n <= y:
            dp[i+n] = min(dp[i+n], dp[i]+1)

    return dp[y] if dp[y] != float('inf') else -1


solution(10, 40, 5)
print("🐍 File: programers/154538-2.py | Line: 20 | undefined ~ solution(10, 40, 5)",
      solution(10, 40, 5))
print("🐍 File: programers/154538-2.py | Line: 20 | undefined ~ solution(10, 40, 5)",
      solution(10, 40, 30))
print("🐍 File: programers/154538-2.py | Line: 20 | undefined ~ solution(10, 40, 5)",
      solution(2, 5, 4))
