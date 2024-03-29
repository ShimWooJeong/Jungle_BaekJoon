from collections import deque
#위상정렬
graph = [[],
         [2,3], #1노드
         [4], #2노드
         [4], #3노드
         [5], #4노드
         []] #5노드

def calculate_edge(graph):
    edge_list = [0] * len(graph) # 각 노드의 진입차수를 기록할 리스트

    for edges in graph: # 각 노드의 진입차수 계산
        for node in edges:
            edge_list[node] += 1
    return edge_list

def Topological(graph, node): # 위상정렬 함수
    edge_list = calculate_edge(graph)
    print('edge: ', edge_list)
    q = deque([node]) # 큐에 시작 노드를 넣으면서 시작
    
    while q: # 큐에 노드가 있다면
        node = q.popleft() # 해당 node를 pop해서
        print(node, end=' ') # 출력해줌

        for i in graph[node]: # 해당 노드와 인접한 노드 탐색
            edge_list[i] -= 1 # q.pop해줬으니까 현재 노드랑 연결된 노드들의 진입차수 감소 = edge 삭제와 마찬가지
            if edge_list[i] == 0: # 감소하면서 진입차수가 0이 되었다면 큐에 삽입
                q.append(i)

Topological(graph, 1)
# edge 개수는 graph 내의 숫자를 카운트 해주면 됨
