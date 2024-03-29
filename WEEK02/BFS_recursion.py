from collections import deque
#N = int(input())
graph = [[], #노드를 1부터 시작하기 위해서 처음은 비워두기
         [2, 3, 5], #1노드
         [1, 4], #2노드
         [1, 4, 5], #3노드
         [2, 3, 7], #4노드
         [1, 3, 6], #5노드
         [5], #6노드
         [4]] #7노드 

visited = [False] * (len(graph))
q = deque() #양쪽에서 삽입/삭제 가능

def BFS(graph, node):
    q.append(node) #시작 노드 먼저 큐에 삽입
    visited[node] = True #방문처리 해주고
    
    while q:
        node = q.popleft() #큐에서 pop해줌
        print(node, end=' ')
        for i in graph[node]: #인접한 노드 중에
            if not visited[i]: #방문하지 않은 노드가 있다면
                q.append(i) #큐에 삽입해주고
                visited[i] = True

BFS(graph, 1)

