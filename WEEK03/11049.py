import sys

N = int(sys.stdin.readline())
p = [] #행렬의 차원을 나타냄

for _ in range(N):
    p.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 if i == j else float('inf') for j in range(N)] for i in range(N)] #N*N 행렬
#최소 곱셈 연산 횟수 저장할 2차원 배열 초기화

def matrix_chain(n):
    for r in range(1, N):
        for i in range(N-r):
            j = i+r
            for k in range(i, j): #회전하기 위한?
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+p[i][0]*p[k][1] *p[j][1])
    print(dp[0][N-1])

matrix_chain(N)