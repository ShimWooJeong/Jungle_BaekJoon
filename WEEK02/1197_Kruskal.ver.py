#최소 스패닝 트리 -> Kruskal or Prim
#Kruskal 활용
import sys

V, E = map(int, sys.stdin.readline().split()) #V: 정점 수, E: 엣지 수

edges = []
parent = [i for i in range(V+1)] #리스트 처음 [0]으로 걍 두고 시작하는 거 잊지 말기ㅠ range(1, V+1) 아님XX
minimum_cost = 0

def find(parent, x): #부모 찾는 코드
    if parent[x] == x:
        return parent[x]
    else:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b): #합치는 코드
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split()) #A-B의 가중치=C
    edges.append((C, A, B))

edges.sort() #가중치를 기준으로 오름차순으로 정렬

for i in range(E):
    C, A, B = edges[i]
    if find(parent, A) != find(parent, B): #부모가 다르다면
        minimum_cost += C
        union(parent, A, B)

print(minimum_cost)
