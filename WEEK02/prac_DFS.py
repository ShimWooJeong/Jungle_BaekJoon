# 그래프를 코드 상에 표현하는 방법
# 1. 인접 행렬
# graph = [[0, 1, 1, 1], #0번째 노드와 1,2,3번째 노드가 연결되어 있다는 의미
#          [1, 0, 0, 1], #1번째 노드는 0,3번째 노드와 연결되어 있다는 의미
#          [1, 0, 0, 1], #2번째 노드는 0,3번째 노드와 연결되어 있다는 의미
#          [1, 1, 1, 0]] #3번째 노드는 0,1,2번째 노드와 연결되어 있다는 의미
# 각 행과 열은 노드를 의미함
# 가중치 그래프의 경우엔 1이 아닌 다른 값을 넣어 표현할 수 있음
# 특정 노드 간 연결 정보를 찾아야 하는 경우 유리 ex. graph[i][j]로 i와 j가 연결되었는지 확인

# 2. 인접 리스트
# graph = [
#          [1, 2, 3], # 0-1,2,3 연결
#          [0, 3], # 1-0,3 연결
#          [0, 3], # 2-0,3 연결
#          [0, 1, 2] # 3-0,1,2 연결
# ]
# 각각의 인덱스에 해당하는 노드에 연결된 노드들을 리스트 형태로 저장
# 가중치 그래프의 경우 연결 정보에 튜플형태나 다른 방식으로 가중치를 추가 입력해줘야 함
# 모든 연결정보를 찾아야 하는 경우 유리

# 구현1. 인접행렬 + 스택
N, M, V = map(int, input().split()) # N: 정점 개수, M: 간선 개수, V: 탐색 시작 정점
matrix = [[0] * (N+1) for _ in range(N+1)] #인접행렬 생성, N+1인 이유는 노드의 Index가 1부터 시작하기 때문
visited = [False] * (N+1) #방문 리스트

for _ in range(M):
    f, t = map(int, input().split()) #f와 t를 연결하겠다는 의미
    matrix[f][t] = matrix[t][f] = 1 #f와 t 사이에 간선이 생긴다는 의미로 1로 설정

print(matrix)

def DFS(matrix, i, visited): # i=탐색할 노드
    stack=[i] #탐색 시작을 할 노드 삽입
    while stack:
        value = stack.pop() #스택에 있는 값 pop
        if not visited[value]: #해당 값이 방문한 적 없는 노드라면
            print('방문 해서 출력: ', value) #방문하면서 값 출력  end=' '
            visited[value] = True
        for j in range(len(matrix)-1, -1, -1):
            #스택에 특성상 LIFO 이기 때문에 나중에 들어간 더 높은 값이 먼저 나오게 됨
            #본래 (1, len(matrix))로 쓰면 2,3,4 순으로 쌓이고 4부터 pop되기 때문에
            #반대로 순회하는 거
            if matrix[value][j] == 1 and not visited[j]: #matrix[value][j] == 1은 value노드에서 인접한 노드라는 의미
                print(f'스택에 넣을 값: {j},', '스택 값: ', stack)
                stack.append(j)

DFS(matrix, V, visited)

# 구현2. 인접리스트 + 재귀 -> 똑같고 함수 부분에 재귀만 넣어주면 됨
def DFS(maxtrix, i, visited):
    visited[i] = True
    print(i, end=' ')
    for j in range(len(matrix[i])):
        if maxtrix[i][j] == 1 and not visited:
            DFS(maxtrix, j, visited[j])





