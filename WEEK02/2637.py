import sys
from collections import deque
## 풀어야 댐
## 개수를 가중치로 두고 풀어보기
N = int(sys.stdin.readline()) # 기본 or 중간 부품 번호
M = int(sys.stdin.readline()) # 완제품 번호

edge_list = [[] for _ in range(N+1)] #엣지 정보: Y가 K의 가중치로 X를 가리킴
indegree_list = [0] * (N+1) #진입차수 리스트, 0인 애들이 기본 부품
q = deque()

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    # X를 만드는데 중간/기본 부품 Y가 K개 필요하다는 의미
    edge_list[Y].append((X, K))
    indegree_list[X] += 1 # 진입차수

print(edge_list)
print(indegree_list)

for i in range(1, N+1):
    if indegree_list[i] == 0:
        q.append(i)

cnt_list = [0] * (N+1)

while q:
    current = q.popleft() 
    for object, parts_cnt in edge_list[current]: #object: 중간 부품 or 완성품, parts_cnt: 필요한 개수
        if indegree_list[current] == 0:
            cnt_list[object]

