case=int(input())

for i in range(case):
    OX= list(map(str,input()))
    num=0
    continues=0
    score=0
    for j in range(len(OX)):
        if OX[j]=='O':
            num+=1
            continues=num
            score+=continues
        if OX[j]=='X':
            num=0
    print(score)
