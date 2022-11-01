# 별찍기 21
case = int(input())

for i in range(case*2):
    if case==1 :
        print('*')
        break
    else:
        for j in range(case):
            if i%2==0:
                if j%2==0:
                    print('*',end='')
                else:
                    print(' ',end='')
            else:
                if j%2==0:
                    print(' ',end='')
                else:
                    print('*',end='')
    print()
