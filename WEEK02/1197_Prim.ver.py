import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

visited = [False] * (V+1) #방문 리스트 초기화
edges = [[] for _ in range(V+1)] #엣지 정보 담을 List
heap = [[0, 1]] #[가중치, 노드] 시작 노드에 대한 정보 담아놓고 시작

for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split()) #A-B의 가중치 = C
    edges[A].append([C, B]) #무방향 그래프니까
    edges[B].append([C, A]) #양쪽 다 갈 수 있어야 함 -> 두 경우 모두 생각해서 append

minimum_cost = 0

while heap: #힙이 빌 때까지
    next_cost, next_node = heapq.heappop(heap) #가장 가중치가 작은 경로 pop됨
    if not visited[next_node]: #해당 노드가 방문하지 않았던 노드라면
        visited[next_node] = True #방문처리 하고
        minimum_cost += next_cost #가중치 합해주기
        for i in edges[next_node]: #A의 인접 노드들에 대한 정보 push 해주기
            heapq.heappush(heap, i) 

print(minimum_cost)