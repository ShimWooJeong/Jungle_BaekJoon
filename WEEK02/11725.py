import sys
from collections import deque

N = int(sys.stdin.readline()) #노드 개수

edges = [[0] for _ in range(N+1)]
parent = [0] * (N+1) #부모 기록 리스트

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b) #무방향 그래프이니까 양쪽 다
    edges[b].append(a) #두 정점의 linked list에 각각 저장해줌

q = deque()
q.append(1)

while q:
    current = q.popleft()
    for i in edges[current]:
        if parent[i] == 0:
            parent[i] = current
            q.append(i)

for i in parent[2:]:
    print(i)
###이건 BFS 이용해서 푸는 거, 나중에 DFS 이용해서 풀어보기

###### 당연하지만 시간초과 남ㅎㅎ;; 그래도 테스트 케이스 답은 ㄴㅏ옴...
# for i in range(N-1):
#     a, b = map(int, sys.stdin.readline().split()) #a와 b는 연결 노드
#     edges.append((a, b))

# tree = [[] for i in range(N+1)]
# check = [False] * (N+1)
# check[1] = True

# for i in range(N-1):
#     a, b = edges[i]
#     if check[a] == True: #이미 트리에 구성된 노드라면
#         tree[a].append(b) #둘 중 트리에 없는 노드가 해당 노드의 자식이 됨
#         check[b] = True
#     elif check[b] == True:
#         tree[b].append(a)
#         check[a] = True

# for i in range(len(tree)): #리스트 다 돌면서 i가 j번 째 서브 리스트에 있다면 출력
#     for j in range(len(tree)):
#         if i in tree[j]:
#             print(j)