# 동전 0
case, total = map(int, input().split())
coins = []
for _ in range(case):
    coins.append(int(input()))
coins.sort(reverse=True)

cnt = 0
for i in coins:

    if total//i != 0:
        tmp = total//i
        cnt += tmp
        total = total % i
print(cnt)
