import sys
#외판원 순회
#각 도시를 방문했는지의 여부 = 비트마스킹 활용
#현재 도시에서의 최소비용 = DP 활용
#도시를 방문하는 것 = DFS 활용

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#도시 간 이동 비용을 나타내는 2차원 리스트

ans = 99 #최솟값 구하기 위한 변수, 비교를 위해 무제한으로 설정

dp = [[ans for _ in range((1<<N)-1)] for _ in range(N)] #(1<<N)-1은 도시가 N개일 때 모든 부분 집합 개수를 의미

def dfs(start, visited):
    if visited == (1<<N)-1: #모든 도시를 방문했다면
        if graph[start][0]: #마지막 도시에서 시작 도시인 0으로 갈 수 있다면
            return graph[start][0]
        else:
            return ans #갈 수 없으면 그 경로는 말짱 꽝;;;
    if dp[start][visited] != ans: #이미 최소비용이 계산되었다면
        return dp[start][visited]
    
    for i in range(1, N): #0번은 출발 도시기 때문에 1부터 탐색
        if graph[start][i] == 0: #갈 수 없다면 (0이면 길이 없다는 의미)
            continue
        if visited & (1<<i): #이미 가봤다면
            continue
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + graph[start][i])
    return dp[start][visited]

print(dfs(0, 1)) #0번 째 도시부터 방문(시작은 상관 없음 어차피 사이클), 0번째 도시 방문 처리(=0001이니까 1)
print(*dp, sep='\n')