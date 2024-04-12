import sys

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(*graph, sep='\n')