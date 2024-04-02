import sys

n, m = map(int, input().split()) #n: 노드 개수, m: 간선 개수
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m): #간선 수 만큼 데이터 받아서 저장
    start_node, end_node, cost = map(int, input().split())
    graph[start_node][end_node] = cost #start->end 노드로 가는데 드는 비용 cost

for i in range(1, n+1):
    graph[i][i] = 0 #자기 자신에서 자기 자신까지는 0

for k in range(1, n+1): #k는 거쳐갈 노드
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            #만약 i->j로 갈 때, 그냥 직통으로 가는 것과 i->k를 가고 k->j 즉 k를 들렀다 가는 것 중 더 최솟값으로 갱신
            #모든 경우의 수를 계산
            #1->2, 1->2 ... 2->1, 2->2, 2->3... 경로에서 k를 거치는 게 더 최소라면 갱신하는 뉘앙스

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF and graph[i][j] != 0:
            print(f'{i}번 노드부터 {j}번 노드까지의 최단 거리: ', graph[i][j])

# 4 5
# 1 2 1
# 1 3 3
# 1 4 4
# 2 4 2
# 3 4 1   

# for i in range(1, n+1) : #모든 경우의 수에 대해
#     for j in range(1, n+1) :
#         if graph[i][j] == INF : #도달할 수 없다면
#             print("0", end=" ") # 0 출력
#         else :
#             print(graph[i][j], end=" ") #도달할 수 있다면 최단 경로 출력
#     print() 