import sys
N, M = map(int, sys.stdin.readline().split()) #N: 정점 개수, M: 간선 개수

edges = []
parent = [i for i in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split()) # 간선의 양 끝 점 u, v
    edges.append((u, v))

def find(parent, x):
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    u, v = edges[i]
    if find(parent, u) != find(parent, v):
        union(parent, u, v) 
## union함수 만들 필요 없이 max[u, v] = min[u, v] 해주면 한 번에 다 함!

parent_type = []

for i in range(1, N+1): #이거 해줘야 모든 부모가 업데이트 됨
    find(parent, i) #마지막에 부모를 업데이트해주지 않으니까!

for i in range(len(parent)):
    if parent[i] not in parent_type and parent[i] != 0:
        parent_type.append(parent[i])

print(len(parent_type))
    