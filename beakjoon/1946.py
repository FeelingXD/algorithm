# 신입사원
import sys
input = sys.stdin.readline
if __name__ == "__main__":

    tc = int(input())
    for _ in range(tc):
        n = int(input())
        data = []
        for _ in range(n):
            a, b = map(int, input().split())
            data.append((a, b))
        data.sort(key=lambda x: x[1])
        min = data[0][0]

        count = 1
        for i in range(1, n):
            if data[i][0] < min:
                min = data[i][0]
                count += 1
        print(count)
