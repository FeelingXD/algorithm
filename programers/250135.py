# [PCCP 기출문제] 3번 시계
def cal_zero_to_target(h,m,s):
    # degree 360 도 기준으로 각 시 분 초침에대한 각도를구함 360을기준
    hDegree,mDegree,sDegree=(h*30+0.5*m+s*1/120)%360,(m*6+0.1*s)%360,(s*6)
    ret=-1
    
    if sDegree>=mDegree: ret+=1
    if sDegree>=hDegree: ret+=1
    
    ret +=(h*60+m)*2 #분당 두번만남 초침 시/분 침이
    ret -=h
    if h>=12: ret-=2
    print(ret)
    return ret
    

def solution(h1, m1, s1, h2, m2, s2):
    ans=cal_zero_to_target(h2,m2,s2)-cal_zero_to_target(h1,m1,s1)
    if (h1==0 or h1==12) and m1==0 and s1==0 :ans+=1
    return ans