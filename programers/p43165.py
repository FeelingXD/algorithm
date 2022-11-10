def solution(numbers, target):
    answer = 0
    maxidx=len(numbers)
    def dfs(idx,result):
        if idx==maxidx :
            if target==result:
                nonlocal answer
                answer +=1
            return
        else:
            dfs(idx+1,result+numbers[idx])
            dfs(idx+1,result-numbers[idx])
    dfs(0,0)
    return answer
        