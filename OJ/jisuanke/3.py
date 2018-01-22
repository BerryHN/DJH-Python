import math
flag=True
x=int(input())
if x<2:
    print('NO')
else:
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            flag = False
            print('NO')
            break
    if(flag):
        print('YES')
    
