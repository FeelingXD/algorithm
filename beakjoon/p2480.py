
inputs = list(input().split())
case =set(inputs)
if len(case)==1:
    result= 10000+int(set(inputs).pop())*1000
elif len(case)==2:
    dic = {int(key): inputs.count(key) for key in inputs}
    result= 1000+[key for key , value in dic.items() if value==2][0]*100
else :
    result= int(max(case))*100
print(result)