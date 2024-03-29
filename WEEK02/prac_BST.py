class Node: #노드 생성
    def __init__(self, value):
        self.value = value #노드 값 지정
        self.left = None #왼쪽 노드 공간 생성
        self.right = None #오른쪽 노드 공간 생성

class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self, value):
        self.current_node = self.root #current node를 root 노드로 초기화

        while True:
            if value < self.current_node.value: #넣으려는 값이 루트 노드보다 작을 때
                if self.current_node.left != None: #왼쪽 자식 노드가 이미 있다면
                    self.current_node = self.current_node.left #왼쪽 자식 노드를 current node로 갱신, 그러니까 왼쪽으로 더 내려가겠다는 의미
                else: #왼쪽 자식 노드가 없다면
                    self.current_node.left = Node(value) #넣으려는 값의 노드를 왼쪽에 삽입
                    break #삽입 했으니까 break
            else: #넣으려는 값이 루트 노드보다 클 때
                if self.current_node.right != None: #오른쪽 자식 노드가 이미 있다면
                    self.current_node = self.current_node.right #오른쪽 자식 노드를 current node로 갱신, 그러니까 오른쪽으로 더 내려가겠다는 의미
                else: #오른쪽 자식 노드가 없다면
                    self.current_node.right = Node(value) #넣으려는 값의 노드를 오른쪽에 삽입
                    break #삽입 했으니까 break
    
    def search(self, value):
        self.current_node = self.root #current node를 root 노드로 초기화

        while self.current_node:
            if self.current_node.value == value: #현재 노드의 값이 찾으려는 값이랑 일치할 때
                return True
            elif self.current_node.value < value: #현재 노드의 값이 찾으려는 값보다 작을 때
                self.current_node = self.current_node.left #왼쪽 노드로 옮겨서 탐색
            else: #현재 노드의 값이 찾으려는 값보다 클 때
                self.current_node = self.current_node.right #오른쪽 노드로 옮겨서 탐색
        return False #다 돌았는데도 없을 때 False 리턴

    # 테스트 필요    
    # def post_order(self, root):
    #     if root is None:
    #         pass
    #     else: 
    #         self.post_order(root.left)
    #         self.post_order(root.right)
    #         print(root.value)

N = int(input())
