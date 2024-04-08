import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# N: 노드 개수, M: 엣지 개수
INF = 1e9
graph = [[] for _ in range(N+1)]
min_cost = [INF] * (N+1) # 최단 거리 기록

for _ in range(M):
    s, e, cost = map(int, sys.stdin.readline().split())
    # s->e까지의 cost: 가중치
    graph[s].append((e, cost))

start, end = map(int, sys.stdin.readline().split())
# start: 출발 노드, end: 도착 노드

def Dijkstra(graph, start):
    q = []
    heapq.heappush(q, (0, start)) # heap에 넣을 때 cost/node 순임, 헷갈리기 쉬운 부분!!!
    min_cost[start] = 0 #최단 거리 테이블 초기화

    while q:
        cost, current_node = heapq.heappop(q)

        if min_cost[current_node] < cost: # 이미 최단 거리 기록이 더 작으면 continue
            continue

        for next_node, next_cost in graph[current_node]: # 인근 노드에 대해서 최단 거리 확인
            new_distance = cost + next_cost
            if new_distance < min_cost[next_node]:
                min_cost[next_node] = new_distance
                heapq.heappush(q, [new_distance, next_node])

Dijkstra(graph, start)
print(min_cost[end])