# 스킬 트리
def solution(skill, skill_trees):
    dic = {}
    for i in range(len(skill)):
        dic[skill[i]] = i+1
    print(dic)
    answer = len(skill_trees)
    for i in skill_trees:
        tmp = 0
        for j in range(len(i)):
            if tmp-dic.get(i[j], 0) < -1:
                answer -= 1
                break
            tmp = max(tmp, dic.get(i[j], 0))
    return answer
