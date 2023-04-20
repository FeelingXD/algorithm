# 덩치 브루트 포스
case = int(input())
prof = []
for _ in range(case):
    prof.append(list(map(int, input().split())))

for i in prof:
    rank = 1
    for j in prof:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
