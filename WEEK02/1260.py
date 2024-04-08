import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] * (N+1) for _ in range(N+1)]
#0번 째는 비워둠

for _ in range(M): #인접 리스트로 만들어줌
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) #무방향이니까 각각 넣어줌
    graph[b].append(a)
    graph[a].sort() #방문할 수 있는 정점이 여러개면 작은 걸 먼저 방문해야 하니까
    graph[b].sort() #정렬 해줘야 함

visited_dfs = [False] * (N+1)

def DFS(graph, node):
    visited_dfs[node] = True
    print(node, end=' ')

    for i in graph[node]: #인접한 노드들 재귀 방문
        if not visited_dfs[i]:
            DFS(graph, i)

visited_bfs = [False] * (N+1)
q = deque()

def BFS(graph, node):
    q.append(node) #시작 노드 삽입
    visited_bfs[node] = True #방문 처리

    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True

DFS(graph, V)
print()
BFS(graph, V)