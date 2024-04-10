import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#도시 간 이동 비용을 나타내는 2차원 리스트

ans = 1e9 #최솟값 구하기 위한 변수, 비교를 위해 무제한으로 설정

def dfs(start, current, cost): #출발 도시/현재 위치 도시/현재까지 이동 비용
    global ans, visited

    if all(visited): #모든 도시를 방문했다면
        if graph[current][start] != 0: #출발 도시로 되돌아올 수 있다면
            ans = min(ans, cost+graph[current][start]) #최솟값 갱신
        return
    
    for next in range(N): #각 도시에서 출발해서 dfs 함수 호출
        if visited[next] == False and graph[current][next] != 0: #다음 도시에 방문하지 않았고, 그 도시로 이동할 수 있는 경로가 있다면 
            visited[next] = True #해당 도시 방문 처리
            dfs(start, next, cost + graph[current][next]) #이동 비용 갱신해주고, 다음 도시로 이동 재귀
            visited[next] = False #해당 경로에 대해 DFS탐색이 끝나면 다시 방문하지 않은 것으로 표기하기 위해 backtracking

for i in range(N):
    visited = [False] * N #각 출발 도시마다 visited 리스트를 초기화 해주기 위해 for문 안에 둬야 함
    visited[i] = True
    dfs(i, i, 0)

print(ans)
