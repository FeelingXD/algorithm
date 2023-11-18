# 광물 캐기
def solution(picks, minerals): # match case 풀이
    answer=0    
    able_pick=sum(picks)*5
    
    if len(minerals)>able_pick:
        minerals=minerals[:able_pick]
    new_minerals=[[0,0,0] for _ in range(len(minerals)//5+1)]
    
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1    
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            new_minerals[i//5][2]+=1
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    for minerals in new_minerals:
        dia,iron,stone=minerals
        for i in range(len(picks)):
            if picks[i]:
                match i:
                    case 0:
                        answer+=sum(minerals)
                        picks[i]-=1
                        break
                    case 1:
                        answer+=(5*dia)+iron+stone
                        picks[i]-=1
                        break
                    
                    case 2:
                        answer+=(25*dia)+(5*iron)+stone
                        picks[i]-=1
                        break
    return answer

def solution(picks, minerals): # if 문풀이
    answer=0    
    able_pick=sum(picks)*5
    
    if len(minerals)>able_pick:
        minerals=minerals[:able_pick]
    new_minerals=[[0,0,0] for _ in range(len(minerals)//5+1)]
    
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1    
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            new_minerals[i//5][2]+=1
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    for minerals in new_minerals:
        dia,iron,stone=minerals
        for i in range(len(picks)):
            if picks[i]:
                if i==0:
                        answer+=sum(minerals)
                        picks[i]-=1
                        break
                elif i ==1:
                        answer+=(5*dia)+iron+stone
                        picks[i]-=1
                        break
                    
                else:
                        answer+=(25*dia)+(5*iron)+stone
                        picks[i]-=1
                        break
    return answer


solution([1, 3, 2],	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])