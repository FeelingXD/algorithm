# 돌아온 똥게임
import sys
input =sys.stdin.readline
def solution():
    N,D =map(int,input().split())
    monsters=[]
    weapons=[]
    ans=0
    for _ in range(N):
        t,value=map(int,input().split())
        if t==1:
            monsters.append(value)
        else:
            weapons.append(value)
    monsters.sort()
    weapons.sort(reverse=True)
    
    for monster in monsters:
        if D> monster:
            D+=monster
            ans+=1
        else:
            while weapons:
                D*=weapons.pop()
                ans+=1
                if D > monster:
                    D+=monster
                    ans+=1
                    break
            else:
                break
    print(ans+len(weapons))
    pass

if __name__=="__main__": # 실행되는 부분
    solution()
    pass