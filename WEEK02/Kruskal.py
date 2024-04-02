import sys

node, edge = map(int, input().split())

parent_table = [0] * (node+1) #부모 테이블 초기화

for i in range(1, node+1):
    parent_table[i] = i #처음에 각 노드는 자기 자신을 부모로 가진 상태

def find_parent(parent_table, x): #find 함수: 각 노드(or집합)의 부모 노드를 찾는 함수
    if parent_table[x] == x: #루트 노드(대표 노드)는 자기 자신을 부모로 가짐
        return parent_table[x]
    else: #재귀로 루트 노드를 찾아감
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]

def union(parent_table, a, b): #union 함수: 각 집합을 합쳐주는 함수
    a = find_parent(parent_table, a)
    b = find_parent(parent_table, b)
    if a < b: #보통 작은 노드를 부모로 가짐
        parent_table[b] = parent_table[a] #b의 대표 노드를 a로 설정
    else: ####부모의 부모값을 바꿔줌!!!%%
        parent_table[a] = parent_table[b] #a의 대표 노드를 b로 설정

edges = [] #간선 정보 저장 리스트
total_cost = 0 #최소 신장 트리 합

for _ in range(edge): #간선 정보 입력
    a, b, cost = map(int, input().split()) #a와 b사이의 비용 = cost
    edges.append((cost, a, b))

edges.sort() #간선 비용에 대해 오름차순 정렬

for i in range(edge):
    cost, a, b = edges[i] #오름차순 된 간선들을 차례로
    if find_parent(parent_table, a) != find_parent(parent_table, b): #두 집합의 부모 노드가 같지 않다면
        union(parent_table, a, b) #두 집합을 합치면서, 작은 애를 해당 집합의 부모 노드로 설정
        total_cost += cost #total 간선 비용에 더해줌
    #두 집합의 부모 노드가 같다면 사이클이 발생하니까 안 됨
        
print(total_cost)
