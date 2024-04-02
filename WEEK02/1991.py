import sys

N = int(sys.stdin.readline()) #노드 개수

binary_tree = {}

for _ in range(N):
    node, left, right = map(str, sys.stdin.readline().split())
    #각 노드, 왼쪽 자식, 오른쪽 자식
    binary_tree[node] = ((left, right))

def pre_order(start): #전위 순회: 루트->왼쪽->오른쪽
    if start == '.':
        return
    print(start, end='')
    pre_order(binary_tree[start][0])
    pre_order(binary_tree[start][1])

def in_order(start):#중위 순회: 왼쪽->루트->오른쪽
    if start == '.':
        return
    in_order(binary_tree[start][0])
    print(start, end='')
    in_order(binary_tree[start][1])

def post_order(start): #후위 순회: 왼쪽->오른쪽->루트
    if start == '.':
        return
    post_order(binary_tree[start][0])
    post_order(binary_tree[start][1])
    print(start, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')

