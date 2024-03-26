import sys
from collections import deque
# deque를 쓰지 않으면 시간초과 발생
# 파이썬이 제공하는 collections deque 모듈로 deque() 사용 가능
# deque 쓰면 append/pop 할 때 left인 지 right인지 작성할 수 있음
# pop(0)이 아닌 popleft()로 작성

N = int(input())

queue = deque([])
command = []
for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])
