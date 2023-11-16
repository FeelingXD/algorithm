# 순위 검색
import re
from collections import defaultdict
def make_dic(info):
    dic= defaultdict(list)
    for i in info: # 정보에서 데이터추출하여 dictionary로 치환
        lan,pos,career,food,score=i.split()
        for l in [lan,'-']:
            for p in [pos,'-']:
                for c in [career,'-']:
                    for f in [food,'-']:
                        dic[(l,p,c,f)].append(int(score))
    for k in dic:
        dic[k].sort()
    return dic


def solution(info, query):
    
    answer = []
    dic=make_dic(info)
    
    for q in query:
        q = re.sub(" and","",q).split()
        scores= dic[(q[0],q[1],q[2],q[3])]
        wanted=int(q[-1])
        l,r=0,len(scores)
        while l<r:
            middle=(l+r)//2
            if scores[middle]>=wanted:
                r=middle
            else:
                l=middle+1
        answer.append(len(scores)-l)
        
    return answer