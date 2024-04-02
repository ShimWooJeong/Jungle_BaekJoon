import sys

N = int(sys.stdin.readline()) #컴퓨터 개수 = 노드
E = int(sys.stdin.readline()) #컴퓨터 연결 쌍의 수 = 엣지

edges = []
edges = []
parent = [i for i in range(N+1)]

def find_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for i in range(E):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))

for i in range(E):
    a, b = edges[i]
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[max(a, b)] = parent[min(a, b)]

for i in range(N+1):
    find_parent(parent, i)

print(parent.count(1)-1) #자기 자신 제외해야 하니까 -1

