import sys

N = int(sys.stdin.readline())

tree = {} #딕셔너리

for i in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]
#{'A':['B', 'C'], 'B':['D', '.'], ... } 형식

def pre_order(root): #전위순회: 루트-> 왼쪽-> 오른쪽
    if root != '.': #값이 .이 아니면 출력
        print(root, end='')
        pre_order(tree[root][0]) #왼쪽
        pre_order(tree[root][1]) #오른쪽
    

def in_order(root): #중위순회: 왼쪽->루트->오른쪽
    if root != '.':
        in_order(tree[root][0])
        print(root, end='')
        in_order(tree[root][1])

def post_order(root): #후위순회: 왼쪽->오른쪽->루트
    if root != '.':
        post_order(tree[root][0])
        post_order(tree[root][1])
        print(root, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')