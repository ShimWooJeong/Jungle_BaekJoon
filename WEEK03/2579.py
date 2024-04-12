import sys

N = int(sys.stdin.readline()) #N: 계단 개수

value = [int(sys.stdin.readline()) for _ in range(N)]

dp = [0 for _ in range(N)] #dp[i] = i번 째 계단까지의 최댓값

if N <= 2:
    dp[0] = value[0]
    dp[1] = max(dp[0]+value[1], value[1]) 
    dp[2] = max(dp[0]+value[2], dp[1]-value[0]+value[2])
else:
    dp[0] = value[0] #첫 번째 계단을 오르는 최댓값은 그냥 오르는 거
    dp[1] = max(dp[0]+value[1], value[1]) 
    dp[2] = max(dp[0]+value[2], dp[1]-value[0]+value[2])

    for i in range(3, N):
        dp[i] = max(dp[i-3]+value[i-1]+value[i], dp[i-2]+value[i])
        #연속된 계단 3개는 오를 수 없으므로
        #i-3을 밟고 i-2를 안 밟고 오르는 경우 & i-2를 밟고 i-1을 안 밟고 오르는 경우 중 max
        #i는 무조건 밟아야 하니까, 이전 3개 계단을 모두 고려해야 함

print(dp)
print(dp[-1])