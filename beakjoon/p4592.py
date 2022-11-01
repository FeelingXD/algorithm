output= []
while True:
    inputs = list(map(int,input().split()))
    if inputs[0] == 0:
        break
    else :
        inputs.pop(0)
        output.append(inputs[0])
        for i in range(len(inputs)):
            if output[-1]!=inputs[i]:
                output.append(inputs[i])
        result = ' '.join(map(str,output)) + " $"
        output.clear()
        print(result)
