# 도둑질
def solution(money):
    if len(money) == 3:
        return max(money)
    return max(dp(money[:-1])[-1], dp(money[1:])[-1])


def dp(arr):
    k = [0]*(len(arr))
    k[0] = arr[0]
    k[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        k[i] = max(k[i-1], k[i-2]+arr[i])
    return k
