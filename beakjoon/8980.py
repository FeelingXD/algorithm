# 택배
import sys
input =sys.stdin.readline

def solution():
    N,C=map(int,input().split())
    packages=[C]*(N+1)
    infos=[]
    
    for _ in range(int(input())):
        s,t,box=map(int,input().split())
        infos.append((s,t,box))
    
    infos.sort(key=lambda x:x[1])
    ans=0
    
    for s,t,box in infos:
        min_capa=box   
        for i in range(s,t):
            min_capa =min(packages[i] , min_capa)
        for i in range(s,t):
            packages[i]-=min_capa
        ans+=min_capa #
    print(ans)
    pass
if __name__=="__main__": # 실행되는 부분
    solution()
    pass