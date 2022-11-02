#별찍기 9
case= int(input())
case= case*2-1
for i in range(case):
    if i> case//2 :
        for j in range(case//2-1,-1,-1):
            print(j*' '+(case-2*j)*'*')
        break
    else:
        print(i*' '+(case-2*i)*'*')
