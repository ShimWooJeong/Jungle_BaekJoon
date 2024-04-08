import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
# N: 도시 개수, M: 도로 개수, K: 거리 정보, X: 출발 도시
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)

minimum = [0 for _ in range(N+1)] #각 노드별 X에서 출발할 때의 최단 거리 기록 리스트

def BFS(graph, X):
    visited[X] = True
    q = deque()
    q.append(X)

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                minimum[i] = minimum[node]+1
    return minimum

cnt = 0
min = BFS(edges, X)
for i in range(len(min)):
    if min[i] == K:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)