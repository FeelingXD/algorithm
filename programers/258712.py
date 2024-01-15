# 가장 많이받은 선물
from collections import defaultdict
def solution(friends, gifts):
    
    friend_code = {f:i for f,i in zip(friends,range(len(friends)))}
    print(friend_code)
    
    gift_matrix=[[0]*len(friends) for _ in range(len(friends))]
    gift_score=defaultdict(int)
    answer = 0
    
    for gift in gifts:
        sender,receiver=gift.split()
        
        # 선물 지수 갱신
        gift_score[sender]+=1
        gift_score[receiver]-=1
        
        # 메트리스 갱신
        gift_matrix[friend_code[sender]][friend_code[receiver]]+=1
    
    for friend in friends:
        tmp=0
        
        for other in friends:
            if friend == other:
                continue
            if gift_matrix[friend_code[friend]][friend_code[other]] > gift_matrix[friend_code[other]][friend_code[friend]]:
                tmp+=1
            elif gift_matrix[friend_code[friend]][friend_code[other]] == gift_matrix[friend_code[other]][friend_code[friend]] and gift_score[friend]>gift_score[other]:
                tmp+=1
        answer=max(answer,tmp)
        
    return answer
solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])