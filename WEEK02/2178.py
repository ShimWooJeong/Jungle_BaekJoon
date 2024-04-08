import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
# N: 열, M: 행 -> NxM 배열 만들기

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

def BFS(graph, x, y): # x, y는 시작 지점
    #     상  하  좌  우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    q = deque() # current 주소 저장 목적
    q.append((x,y)) #x,y에서 시작
    while q:
        x, y = q.popleft() #이동할 수 있는 좌표값 pop
        for i in range(4): #상하좌우 체크
            tempx = x + dx[i]
            tempy = y + dy[i]
            if 0<=tempx<N and 0<=tempy<M and graph[tempx][tempy]==1: #좌표 내에서만 이동해야 하니까 0<=<N, 0<=<M
                    q.append((tempx, tempy)) #이동한 위치 저장
                    graph[tempx][tempy] = graph[x][y] + 1 #값이 1인 곳에는 이동 가능하니까 지나는 칸 수 +1 해주고
                    #while문 돌면서 결국 [N-1][M-1]에는 최소 칸 수의 값이 저장되게 됨
                    #좌표가 0,0부터 시작이니까 N-1, M-1
    return graph[N-1][M-1]

cnt = BFS(arr, 0, 0)
            
print(cnt)