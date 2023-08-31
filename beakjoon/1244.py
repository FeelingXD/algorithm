# 스위치 켜고 끄기
import sys
input = sys.stdin.readline
MALE = 1
FEMALE = 2
num_switches = int(input())
switches = list(map(int, input().split()))
cases = int(input())
cnt = 0

for _ in range(cases):
    # 성별 번호
    s, n = map(int, input().split())

    if s == MALE:
        for i in range(n-1, num_switches, n):
            switches[i] = 0 if switches[i] else 1
        pass
    else:
        n -= 1  # 배열인덱스 -1 이므로
        tmp = 0
        while (n-tmp) >= 0 and (n+tmp) < num_switches:
            if switches[n-tmp] == switches[n+tmp]:
                tmp += 1
            else:
                tmp -= 1
                break

        if (n-tmp) < 0 or (n+tmp) >= num_switches:
            tmp -= 1
        for j in range(n-tmp, n+tmp+1):
            switches[j] = 0 if switches[j] else 1

for i in range(num_switches):
    print(switches[i], end=' ')
    cnt += 1
    if cnt % 20 == 0:
        print('')
