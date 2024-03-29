# 트리 구현하는 방법: 사전(dictionar) 활용
# root를 key로, left/right 자식들을 value로 할당
# tree = {}
# tree["A"] = "B", "C" => {"A": ("B", "C")}
# tree의 인덱스는 key로, 저장되는 값은 value로 사전에 저장

N = int(input())
tree = {}

for i in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 한 번 재귀할 때마다 탐색을 한 번 더 한다는 의미로 생각하기
# 함수 속 재귀로 ~order(tree[root][0])은 재귀함수로 왼쪽 끝까지 탐색
            #~oder(tree[root][1])은 재귀함수로 오른쪽 끝까지 탐색

def preorder(root): #전위 순회: 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리
    if root != '.': # root가 비어있지 않으면
        print(root, end='') #부모 출력(첫 번째 들어오면 root node)
        preorder(tree[root][0]) #재귀하면서 left가 새로운 root가 됨
        preorder(tree[root][1]) #재귀하면서 right가 새로운 root가 됨

def inorder(root): #중위 순회: 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
    if root != '.':
        inorder(tree[root][0]) #왼쪽 먼저 탐색
        print(root, end='')
        inorder(tree[root][1]) #오른쪽 탐색

def postorder(root): #후위 순회: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')