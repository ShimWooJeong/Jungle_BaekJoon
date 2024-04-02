import sys
from collections import deque

#K = int(sys.stdin.readline())
graph = []
#for _ in range(K):
V, E = map(int, sys.stdin.readline().split())
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph.append((u, v)) #무방향인 경우 양쪽 각각
    graph.append((v, u))

visit = [False] * (V+1)
q = deque()

def DFS(graph, node):
    