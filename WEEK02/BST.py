class Node:
    def __init__(self, value):
        self.value = value #노드 값 지정
        self.left = None #왼쪽 자식 노드 공간 생성
        self.right = None #오른쪽 자식 노드 공간 생성
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        insert_node = Node(value)

        if self.root == None:
            self.root = insert_node
            return

        current_node = self.root #current node를 root 노드로 초기화

        while True:
            if current_node.value > value:
                # 넣으려는 값이 현재 노드값보다 작다, 왼쪽 서브트리로 가야 함
                if current_node.left != None: # 근데 왼쪽 자식 노드가 이미 있다면
                    current_node = current_node.left #왼쪽 자식 노드를 current로 갱신, 왼쪽으로 더 가겠다는 의미
                else: # 왼쪽이 비어있다, 왼쪽에 새 노드 생성
                    current_node.left = Node(value)
                    break
            else: # 넣으려는 값이 현재 노드값보다 크다, 오른쪽 서브트리로 가야 함
                if current_node.right != None: # 근데 오른쪽 자식 노드가 이미 있다면
                    current_node = current_node.right # 오른쪽 자식 노드를 current로 갱신, 오른쪽으로 더 가겠다는 의미
                else: # 오른쪽이 비어있다, 오른쪽에 새 노드 생성
                    current_node.right = insert_node
                    break

    def search(self, value): #검색
        current_node = self.root #current node를 root 노드로 초기화

        while current_node:
            if current_node.value == value:
                #현재 노드 값이 찾으려는 값과 동일하다 = True:있음
                return True
            elif current_node.value < value: #찾으려는 값이 노드 값보다 클 때
                current_node = current_node.right #오른쪽 노드로 옮겨서 탐색
            else: #찾으려는 값이 노드 값보다 작을 때
                current_node = current_node.left #왼쪽 노드로 옮겨서 탐색
        return False
        #끝까지 탐색해서 root = None이 되면 while문 빠져나오고
        #못 찾았다는 의미니까 False 반환


    def delete(self, value):
        current_node = self.root
        parent_node = self.root
        searched = False

        #삭제할 노드가 있는지 없는지부터 파악
        while current_node:
            if current_node.value == value: #찾으려는 값과 일치, True 반환
                searched = True
                break
            elif current_node.value < value:
                #찾으려는 값이 노드보다 크면 오른쪽 다시 탐색하기 위해 current_right로
                #부모 노드는 현재 탐색한 값, current_node는 다음 탐색할 값
                parent_node = current_node
                current_node = current_node.right
            else:
                #찾으려는 값이 노드보다 작으면 왼쪽 다시 탐색하기 위해 current_right로
                parent_node = current_node
                current_node = current_node.left
        
        if searched == False: #검색해봤는데 없다면 삭제할 노드가 없다는 의미로 False 반환
            return False
        
        #검색해봤는데 있다
        #위에서 검색하면서 이미 self.current 노드는 삭제할 값을 가지고 있는 노드가 됐음
        #또한 parent값도 current_node 전 탐색한 값이기 때문에
        #self.current_node의 부모값으로 설정되어있음

        #Case1) 리프 노드인 경우: 삭제하려는 값의 왼쪽과 오른쪽이 None
        #-> 삭제하려는 값이 부모값보다 작다면 왼쪽/크다면 오른쪽을 None처리
        if current_node.left == None and current_node.right == None:
            if parent_node.value < value: #값이 부모보다 크니까 오른쪽에 있음, None처리
                parent_node.right = None
            else: 
                parent_node.left = None #값이 부모보다 작으니까 왼쪽에 있음, None처리
        
        #Case2) 자식을 한 개만 갖고 있는 경우: 왼쪽만 None이거나 오른쪽만 None이거나.
        #-> 삭제하려는 값의 부모 노드가 삭제하려는 값이 가리키는 자식을 가리키도록(또 삭제하려는 값이 가리키는 브랜치도 None 처리)
        #근데 부모의 왼쪽/오른쪽 어느 브랜치로 연결해야 할 지 모르니까 부모 value와 삭제할 값 value 비교 필요
        #부모의 왼쪽에 있었다면, 왼쪽 브랜치로 연결해야 하고
        #부모의 오른쪽에 있었다면, 오른쪽 브랜치로 연결해야 함        
        elif current_node.left == None or current_node.right == None:
            if parent_node.value < value: #부모값보다 크다면 오른쪽에 있었던 거니까 부모의 오른쪽이 가리키도록
                if current_node.left == None: #삭제하려는 값이 오른쪽 자식을 갖고 있음
                    parent_node.right = current_node.right #부모 right가 그 자식을 가리키도록
                    #current_node.right = None #current의 right를 None처리 해주며 삭제됨
                elif current_node.right == None: #삭제하려는 값이 왼쪽 자식을 갖고 있음
                    parent_node.right = current_node.left
                    #current_node.left = None #current의 left를 None처리 해주며 삭제됨
            else: #부모값보다 작다면 왼쪽에 있었던 거니까 부모의 왼쪽이 가리키도록
                if current_node.left == None: #오른쪽 자식만 갖고 있음
                    parent_node.left = current_node.right
                    #current_node.right = None
                else: #왼쪽 자식만 갖고 있음
                    parent_node.left = current_node.left
                    #current_node.left = None
            del(current_node)
            return
        #Case3) 자식을 두 개 갖고 있는 경우
        #-> 삭제하려는 노드의 value를 기준으로 Lmax(왼쪽 서브트리의 최댓값) or Rmin(오른쪽 서브트리의 최솟값)을 구함 = 여기선 그냥 Rmin으로 했음
        #삭제하려는 값의 부모 노드가 해당 Rmin을 가리키도록(current_parent->Rmin)
        #Rmin의 각 왼/오에 삭제하려는 노드의 왼/오를 그대로 붙여줌
        #마지막으로 삭제 노드의 왼/오를 None으로 만들어서 삭제
        #Rmin랑 Rmin_parent 찾고 난 후, 삭제하려는 값이 parent의 왼/오에 있냐에 따라서 parent가 Rmin를 (왼or오)브랜치로 연결해주기
        elif current_node.left != None and current_node.right != None:
            Rmin_node = current_node.right #Rmin/Rmin_parent를 self.current_node의 오른쪽 노드로 설정
            Rmin_parent_node = Rmin_node 

            while Rmin_node.left != None: #Rmin를 찾으려면 맨 왼쪽에 있는 애를 찾아야 함, 최솟값이니까
                Rmin_parent_node = Rmin_node #left가 있다면 더 작은 최솟값이 있다는 거니까
                Rmin_node = Rmin_parent_node.left #왼쪽 값으로 Rmin을 이동하면서 기존 Rmin은 부모가 됨
                #Rmin_parent_node = temp 
            #while문 벗어나면 Rmin_node가 오른쪽 서브트리의 최솟값이 됨
            if parent_node.value < value: #삭제 노드가 부모 노드보다 큰 경우, 오른쪽 연결
                parent_node.right = Rmin_node
            else: #삭제 노드가 부모 노드보다 작은 경우, 왼쪽 연결
                parent_node.left = Rmin_node

            if Rmin_node.left == None and Rmin_node.right == None: #Rmin이 자식이 없는 경우
                Rmin_parent_node.left = None #Rmin/Rmin_parent 연결 관계 끊기
                Rmin_node.left = current_node.left #Rmin에 삭제 노드 왼/오 연결
                Rmin_node.right = current_node.right
            elif Rmin_node.left == None and Rmin_node.right != None: #Rmin이 오른쪽 자식이 있는 경우
                #Rmin_parent_node.left = None #Rmin/Rmin_parent 연결 관계 끊기
                Rmin_node.left = current_node.left #Rmin에 삭제 노드 왼/오 연결
                Rmin_node.right = current_node.right
                #Rmin의 오른쪽 자식을 Rmin의 부모 노드 왼쪽에 붙여주기
                #어차피 Rmin이 parent보다 작으니까 왼쪽에 붙여줘야함

            del(current_node) #삭제 노드 제거
            return
    
    def inorder(self):
        stack = []
        current_node = self.root

        while((current_node is not None) or (len(stack) != 0)):
            if(current_node is not None):
                # print("current node:" + str(current_node.value))
                # print("current left:" + str(current_node.left.value))
                stack.append(current_node)
                current_node = current_node.left
            else:
                parent_node = stack.pop()
                print(parent_node.value, end=' ')
                current_node = parent_node.right

    def preorder(self):
        stack = []
        current_node = self.root
 
        while((current_node != None) or (len(stack) != 0)):
            if current_node != None:
                print(current_node.value, end=' ')
                stack.append(current_node)
                current_node = current_node.left
            else:
                parent_node = stack.pop()
                current_node = parent_node.right 



bst = BST()
bst.insert(6)
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(8)
bst.insert(7)
bst.insert(11)
bst.insert(10)
bst.insert(9)
#bst.inorder()
# print('preorder: ', end=' ')
bst.delete(8)
#bst.delete(8)
print('preorder: ', end=' ')
bst.preorder()
print('\ninorder: ', end=' ')
bst.inorder()

# searched_node = bst.search(7)
# if searched_node is not None:
#     print("\nsearch value: " + str(searched_node))
# else:
#     print("There is no data.")

## 참고 사이트 : https://velog.io/@_choongyul/binary-serch-tree

