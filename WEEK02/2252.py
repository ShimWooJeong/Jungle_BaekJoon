import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

edge_list = [[] for _ in range(N+1)]
inDegree_list = [0 for _ in range(N+1)]
q = deque()

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge_list[a].append(b)
    inDegree_list[b] += 1 #진입차수 업데이트... 이렇게 하면 쉽군;; 굳이 cal_indegree 함수 안 만들어도 됨;;

for i in range(1, N+1): #1번째 노드부터
    if inDegree_list[i] == 0: #진입차수가 0이라면
        q.append(i) #큐에 삽입해놓고 시작

while q:
    node = q.popleft()
    print(node, end=' ')
    for i in edge_list[node]:
        inDegree_list[i] -= 1 #pop했으니까 해당 노드가 가리키는 노드의 진입차수 -1
        if inDegree_list[i] == 0:
            q.append(i)
############## 아!@@@@@@!!!! 꼭 a, b 둘이 붙어서 서야 하는 게 아니라
############## 걍 a가 b보다만 앞에 서면 된다는 조건이었음!!!!!!!!!!!@#@#!#@
############## 4-2, 3-1 이렇게 입력 받아도 걍 3-4-1-2로 서도 되는 거였음.....
##############<<메모리 초과로 실패>>
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     edge_list[a].append(b)

# def cal_indegree(edge_list):
#     indegree_list = [0] * (N+1)
#     for edge in edge_list:
#         for node in edge:
#             indegree_list[node] += 1
#     return indegree_list #진입차수 리스트

# def func_line(edge_list):
#     indegree_list = cal_indegree(edge_list)
#     start = indegree_list.index(0, 1)
#     #indegree_list의 1번 index 이후 범위에서 값이 0인 원소 index값 찾기
#     #start는 진입차수가 0인 노드
#     q = deque()
#     q.append(start)
#     while q:
#         node = q.popleft()
#         print(node, end=' ')
#         if not edge_list[node]: # and all(sublist == [] for sublist in edge_list) == False
#             # 만약 탐색하려는 node의 edge_list가 비어있다면,
#             # 떨어져 있는 다른 노드를 탐색하도록 서브 리스트가 비어져있지 않은 노드의 index를 큐에 넣어주는 방법으로 생각 함
#             # 근데 또 이렇게만 하면 같은 노드를 계속해서 넣고 출력하고 무한으로 반복되어서
#             # 큐에서 pop한 다음 진입차수 -1할 때 해당 엣지 리스트의 노드도 remove 해서 다음 q를 돌 때 비어있도록 해줘야 함
#             # 이렇게 엣지 리스트 노드를 remove 해주면 뒤에 다른 서브 리스트가 다 비어있지 않은지는 확인하지 않아도 됨
#             for i in range(len(edge_list)):
#                 if edge_list[i]:
#                     q.append(i)

#         for i in edge_list[node]:
#             indegree_list[i]-=1
#             edge_list[node].remove(i)
#             if indegree_list[i] == 0:
#                 q.append(i)
#             else:
#                 q.append(indegree_list.index(0, 2))

# func_line(edge_list)