def fibo_Interation(n:int): # 반복문 활용
    for i in range(n):
        if i==0 or i==1:
            x.append(1)
        else:
            x.append(x[i-1]+x[i-2])
    return x

def fibo_Recursion(n:int): # 재귀 활용
        if n==0:
             return
        elif n==1 or n==2:
            return 1
        else:
            return fibo_Recursion(n-1)+fibo_Recursion(n-2)


num = int(input())
x = []
# print(fibo_Interation(num))

for i in range(1, num+1):
         x.append(fibo_Recursion(i))

print(x)