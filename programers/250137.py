# [PCCP 기출문제] 1번

def solution(bandage, health, attacks):
    max_health=health
    c_t=0
    a_dic={}
    for attack in attacks:
        t,d=attack
        a_dic[t]=d
    m_k=list(a_dic.keys())[-1]
    
    heal_stack=0
    while c_t<= m_k:
        if a:=a_dic.get(c_t,0):
            health-=a
            heal_stack=0
            if health<=0:
                return-1
        else:
            heal_stack+=1
            health+=bandage[1]
            if heal_stack and bandage[0] <= heal_stack:
                health+=bandage[2]
                heal_stack=0
            health=min(health,max_health)
        c_t+=1

    return health if health >0 else -1 