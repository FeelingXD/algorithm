# 마법의 엘리베이터
def solution(storey):
    storey = list(map(int, list(str(storey))))
    diff = 0
    answer = 0
    for i in range(len(storey)-1, -1, -1):
        if i != 0:
            if (storey[i] == 5 and storey[i-1]+1 > 5) or storey[i]+diff > 5:
                answer += 10-(storey[i]+diff)
                diff = 1
            else:
                answer += storey[i]+diff
                diff = 0
        else:
            if storey[i]+diff > 5:
                answer += 10-(storey[i]+diff)
                diff = 1
            else:
                answer += storey[i]+diff
                diff = 0
    return answer if diff == 0 else answer+1
