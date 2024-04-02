import sys

N, M, V = map(int, sys.stdin.readline().split())

edges = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))
    
 