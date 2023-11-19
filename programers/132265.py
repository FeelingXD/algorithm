from collections import Counter,defaultdict
def solution(topping):
    
    answer=0
    elder_cakes=Counter(topping)
    young_cakes=defaultdict(int)
    len_elder=len(elder_cakes)
    
    for i in range(len(topping)):
        elder_cakes[topping[i]]-=1
        young_cakes[topping[i]]+=1
        if not elder_cakes[topping[i]]:
            len_elder-=1
        if len_elder==len(young_cakes):
            answer+=1
    return answer