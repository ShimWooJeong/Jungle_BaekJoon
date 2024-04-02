import sys
import heapq

INF = int(1e9) # 초기값으로 무한대를 주기 위함

n, m = map(int, input().split()) #n: 노드 개수, m:간선 개수

graph = [[] for i in range(n+1)] #그래프 생성
min_distance = [INF] * (n+1) #최단 거리 기록할 테이블, 무한으로 초기화

for _ in range(m): # 간선 개수만큼 반복문으로 graph에 모든 간선 정보 입력
    current_node, target, cost = map(int, input().split()) #current에서 target까지 가는 비용 cost
    graph[current_node].append((target, cost)) # current_node: 현재 노드, target: 인접 노드, cost: (current->targe)까지 가는데 드는 비용 

def Dijkstra(start):
    q = [] #최소힙으로 사용할 큐
    heapq. heappush(q, (0, start)) #Start 데이터 Push,
    # start까지 가는데 드는 최소 비용 0이라는 의미
    min_distance[start] = 0 #start->start는 0이니까, 최단거리 0으로 초기화

    while q: #큐가 빌 때까지 반복
        cost, current_node = heapq.heappop(q) #최단거리인 노드의 정보(해당 노드까지의 거리, 해당 노드) pop, heapq 최소힙이므로 걍 pop
        #이 current_node를 기준으로 인접 노드 탐색해 최단 거리 갱신하고,
        #그 중에서도 또 최단 거리인 애로 넘어가서 최단 거리 갱신하고, ... 반복

        if min_distance[current_node] < cost: #만약 current 노드까지의 cost가 기존 최단 거리 테이블의 값보다 크다면 갱신하지 않음
            continue
        
        for near_node, near_cost in graph[current_node]: #현재 노드와 연결된 인접 노드들 탐색  
            next_distance = cost + near_cost #현재 노드를 거쳐서 인접 노드로 이동가는 거리

            if next_distance < min_distance[near_node]: #현재 노드를 거쳐 인접 노드로 이동하는 게 기존 최단 거리 테이블에 기록된 값보다 작다면
                min_distance[near_node] = next_distance #최단 경로를 갱신하고
                heapq.heappush(q, [next_distance, near_node]) #해당 노드에 대해 최소힙에 넣어줌
    #return min_distance[1:]
        
Dijkstra(1)

for i in range(1, n+1):
    if min_distance[i] == INF:
        print("INF")
    else:
        print(f'{i}번 노드까지의 최단 거리: ', min_distance[i])

#print(graph)