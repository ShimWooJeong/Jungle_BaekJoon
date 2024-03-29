graph = [[], #노드를 1부터 시작하기 위해서 처음은 비워두기
         [2, 3, 5], #1노드
         [1, 4], #2노드
         [1, 4, 5], #3노드
         [2, 3, 7], #4노드
         [1, 3, 6], #5노드
         [5], #6노드
         [4]] #7노드 

visited = [False] * (len(graph))

def DFS(graph, node):
    visited[node] = True #방문처리 해주고
    print(node, end=' ')
        
    # 인접한 노드들에 대해 재귀 호출
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i)

# 시작 노드를 1로 설정하여 DFS 실행
DFS(graph, 1)
