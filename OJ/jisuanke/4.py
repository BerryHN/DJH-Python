n=int(input())
fib=[0,1]
if n<2:
    print(fib[n])
else:
    for i in range(2,n+1):
        fib.append(fib[i - 1] + fib[i - 2])
    print(fib[n])
