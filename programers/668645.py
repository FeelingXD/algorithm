# 삼각 달팽이
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]  # 삼각형 만들기
    x, y = -1, 0  # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:  # 내려가기
                y += 1
            else:  # 올라가기
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])
