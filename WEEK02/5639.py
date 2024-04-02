import sys
sys.setrecursionlimit(10 ** 6)
# -> 재귀 최대 깊이 설정: 10의 6제곱
# 재귀를 사용해서 푼 문제에 적용
# 파이썬의 기본 재귀 깊이 제한=1,000이라서 제한이 걸릴 때가 있음

nodes = []

while True: # 엔터 들어올 때까지 입력받음
    try:
        nodes.append(int(sys.stdin.readline())) #전위 순회한 값 node 배열에 저장
    except:
        break

def post_order(nodes): #후위: 왼쪽->오른쪽->루트
    if len(nodes) == 0: #종료 조건(node 배열에 아무것도 안 남았을 때)
        return

    left_nodes = [] #왼쪽 서브트리 저장
    right_nodes = [] #오른쪽 서브트리 저장

    root = nodes[0] #전위 순휘 결과였으니까 처음 입력받은 숫자가 root 노드

    for i in range(1, len(nodes)): #0은 루트 노드니까 1부터 node 마지막까지 반복
        if nodes[i] < root: #루트 노드보다 작다면 left_nodes에
            left_nodes.append(nodes[i])
        else: #루트 노드보다 크다면 right_nodes에 저장
            right_nodes.append(nodes[i])

    post_order(left_nodes) #left_nodes=왼쪽 서브 트리에 대해 먼저 재귀로 후위 순회
    post_order(right_nodes) #right_nodes=오른쪽 서브 트리에 대해 재귀로 후위 순회
    print(root) #root노드 출력

post_order(nodes)