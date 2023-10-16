# 양과 늑대
SHEEP = 0
WOLF = 1


def solution(info, edges):
    l = len(info)

    answer = []
    visited = [False]*l

    def dfs(sheep, wolf):
        if sheep > wolf:  # 양이 많을경우 진행
            answer.append(sheep)
        else:
            return
        for s, e in edges:
            if visited[s] and not visited[e]:
                visited[e] = True
                if info[e] == SHEEP:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[e] = False
    visited[0] = 1
    dfs(1, 0)
    return max(answer)
