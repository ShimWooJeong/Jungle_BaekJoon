from collections import deque
#위상정렬
graph = [[],
         [2,3], #1노드
         [4], #2노드
         [4], #3노드
         [5], #4노드
         []] #5노드

# edge 개수는 graph 내의 숫자를 카운트 해주면 됨
def calculate_edge(graph):
    edge_list = [0] * len(graph) # 각 노드의 진입차수를 기록할 리스트
    # 각 노드의 진입차수 계산해 기록
    for edges in graph: #그래프의 각 edge
        for node in edges: #각 edge가 가리키는 노드
            edge_list[node] += 1 #즉 가리켜지는 노드를 세는 것
    return edge_list

def Topological(graph, node): # 위상정렬 함수
    edge_list = calculate_edge(graph)
    print('edge: ', edge_list)
    q = deque([node]) # 큐에 시작 노드를 넣으면서 시작
    
    while q: # 큐가 빌 때까지 반복
        node = q.popleft() # 해당 node를 pop해서
        print(node, end=' ') # 출력해줌

        for i in graph[node]: # 해당 노드가 가리키는 노드
            edge_list[i] -= 1 # q.pop해줬으니까 현재 노드가 가리키는 노드들의 진입차수 감소 = edge 삭제와 마찬가지
            if edge_list[i] == 0: # 감소하면서 진입차수가 0이 되었다면 큐에 삽입
                q.append(i)

Topological(graph, 1)
