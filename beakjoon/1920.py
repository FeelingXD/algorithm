# 수 찾기
case = int(input())
maps = {i: 1 for i in list(map(int, input().split()))}
case = int(input())
given = list(map(int, input().split()))

for i in given:
    print(maps.get(i, 0))
