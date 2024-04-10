import sys

T = int(sys.stdin.readline()) #테스트 케이스

for _ in range(T):
    N = int(sys.stdin.readline()) #동전의 가짓 수
    coins = list(map(int, sys.stdin.readline().split()))
    coins.insert(0, 0)
    M = int(sys.stdin.readline())
    dp = [[0]*(M+1) for _ in range(N+1)]

    for i in range(N+1): #M=0일 경우 다 1로 두기 
        dp[i][0] = 1

    for j in range(1, N+1):
        for i in range(1, M+1):
            dp[j][i] = dp[j-1][i] #윗줄(동전 가짓 수 하나 적은 거)과 똑같은데
            if i-coins[j] >= 0: #만약 새로 고려할 동전이 채울 동전보다 크다면
                dp[j][i] += dp[j][i-coins[j]] #본래 가짓 수에 +해줌

    print(dp[N][M])