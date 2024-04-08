import sys

N = int(sys.stdin.readline()) #정점 수
A = [] #1: 실내, 0: 실외

A.append(list(map(int, sys.stdin.readline().rstrip()[:N])))
# [:N] N개 개수까지만 들어가도록
# A = [[1, 0, 1, 1, 1]]
graph = [[] * (N+1) for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N + 1)
route_count = 0

def DFS(graph, node):
    visited[node] = True
    for i in graph[node]:
        return