import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * M for _ in range(N)] #전체 좌표에 대해서 방문 리스트

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M: #좌표 범위에서 벗어났을 때
        return
    visited[x][y] = True #방문처리
    if graph[x][y] == '-': #'-'일 때 가로 탐색 -> y+1
        if 0<=y+1<M and graph[x][y+1]=='-': #다음으로 이동할 좌표가 범위 안에 있고 -라면
            if visited[x][y+1]==False: #방문하지 않았다면
                DFS(x, y+1) #다음 좌표로 이동해서 재귀 탐색
    if graph[x][y] == '|': #'|'일 때 세로 탐색 -> x+1
        if 0<=x+1<N and graph[x+1][y]=='|': #다음으로 이동할 좌표가 범위 안에 있고 |라면
            if visited[x+1][y]==False: #방문하지 않았다면
                DFS(x+1, y) #다음 좌표로 이동해서 재귀 탐색

cnt = 0
for i in range(N):
    for j in range(M): #전체 좌표에 대해서 탐색
        if graph[i][j] == '-' or graph[i][j] == '|': #탐색하는 좌표가 - 또는 |라면
            if visited[i][j] == False: #방문하지 않았다면
                DFS(i, j) #재귀로 탐색
                cnt += 1 #한 좌표 DFS() 동일한 애들 재귀로 깊게 탐색했으니까 판자 +1

print(cnt)


