import sys

n = int(sys.stdin.readline())

fibo_list = [0] * (n+1)
fibo_list[1] = 1

for i in range(2, n+1):
    fibo_list[i] = fibo_list[i-1]+fibo_list[i-2]

print(fibo_list[n])

# #Top-down: 재귀
# def fibo_recur(n: int):
#     if n<= 1:
#         return n
#     else:
#         return fibo_recur(n-1)+fibo_recur(n-2)
    
# print('재귀: ', fibo_recur(n))
# #재귀는 시간초과 남