# DFS = 깊이 우선 탐색
# [구현 과정]
# 먼저 시작 노드를 방문처리 해주고,
# 해당 노드에 인접한 노드들을 재귀로 방문처리
# (오름차순 정렬이 되어있다는 가정 하에)
# 한 노드를 깊게(끝까지) 탐색한 후에
# 다시 돌아와서 그 다음 노드를 또 깊게 탐색하는 흐름

graph = [[], #노드를 1부터 시작하기 위해서 처음은 비워두기
         [2, 3, 5], #1노드
         [1, 4], #2노드
         [1, 4, 5], #3노드
         [2, 3, 7], #4노드
         [1, 3, 6], #5노드
         [5], #6노드
         [3, 4]] #7노드 

visited = [False] * (len(graph))

def DFS(graph, node):
    visited[node] = True #방문처리 해주고
    print(node, end=' ')
        
    # 인접한 노드들에 대해 재귀 호출
    for i in graph[node]:
        # 시작 노드 1을 넣었을 때 2, 3, 4 중 2를 먼저 끝까지 탐색
        # 2를 깊게 탐색한 다음, 3을 탐색하려하면 이미 2에서 탐색했음
        # 그럼 넘어가고 다음 4 탐색 하면 7까지 모든 노드 탐색 완료
        if not visited[i]:
            DFS(graph, i)

# 시작 노드를 1로 설정하여 DFS 실행
DFS(graph, 1)
