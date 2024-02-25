# 쿼드압축 후 개수 세기
def solution(arr):
    answer = [0, 0]
    length = len(arr)

    def compression(y, x, l):
        start = arr[y][x]
        for row in range(y, y + l):
            for col in range(x, x + l):
                if arr[row][col] != start:
                    l //= 2
                    compression(y, x, l)  # 2사분면
                    compression(y, x + l, l)  # 1사분면
                    compression(y + l, x, l)  # 3사분면
                    compression(y + l, x + l, l)  # 4사분면
                    return
        answer[start] += 1

    compression(0, 0, length)
    return answer
