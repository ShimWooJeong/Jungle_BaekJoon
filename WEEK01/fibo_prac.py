def fibo_iter(n:int):
    x = []
    for i in range(n):
        #print(i)
        if i<=1:
            x.append(1)
        else:
            x.append(x[i-1]+x[i-2])
    return x
        
def fibo_recur(n:int):
    if n <= 1:
        return 1
    else:
        return fibo_recur(n-1)+fibo_recur(n-2)
    
def fibo_generate(n:int):
    x = []
    for i in range(n):
        x.append(fibo_recur(i))
    return x
    
n = int(input())
print('반복문: ', fibo_iter(n))
print('재귀문: ', fibo_generate(n))