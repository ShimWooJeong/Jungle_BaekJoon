## 총 단지 수는 찾는데, 집의 수는 count가 업데이트가 안 됨

import sys

N = int(sys.stdin.readline()) #지도 크기, N*N 행렬 만들기

graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False] * N for _ in range(N)]

    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x < 0 or x >= N or y < 0  or y >= N: #좌표 범위에서 벗어났을 때
        return
    visited[x][y]=True #방문처리
    if graph[x][y] == '1': #탐색하는 좌표가 1일 때 ***좌표가 1일 때 숫자 1 아님, '1' 문자로 탐색***
        global cnt #***test 제출 후 추가해 완성된 코드: cnt 전역 변수로 설정하기***
        cnt += 1 #탐색 시작하는 좌표도 1개로 쳐야 하니까
        for i in range(4): #상하좌우 확인해보기
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]== '1': #만약 다음 탐색할 좌표가 범위 안에 있고
                if visited[nx][ny] == False: #graph[n][y]가 1이고, 방문하지 않았다면
                    DFS(nx, ny) #그리고 끝까지 재귀
    return cnt

cnt_list = []
for i in range(N):
    for j in range(N): #전체 좌표에 대해서 탐색
        if graph[i][j] == '1' and visited[i][j] == False: #탐색하는 좌표가 1이고 방문하지 않았다면
            cnt = 0
            #DFS(i, j, cnt)
            cnt_list.append(DFS(i, j)) #DFS로 탐색해서 한 영역 좌표 개수 카운팅 한 거 넣어주기

cnt_list.sort()
print(len(cnt_list)) #총 단지 수 출력
for i in range(len(cnt_list)):
    print(cnt_list[i]) #정렬된 단지 수 오름차순으로 출력
 