# 게임을 만든 동준이
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    scores = []
    answer = 0
    for _ in range(n := int(input())):
        scores.append(int(input()))
    for i in range(n-2, -1, -1):
        if scores[i] >= scores[i+1]:
            answer += scores[i]-scores[i+1]+1  # 같을경우 + 1 를 해줘야 차이를 둘수있음
            scores[i] = scores[i+1]-1
    print(answer)
