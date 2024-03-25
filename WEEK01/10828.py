import sys
N = int(input())
stack = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push": #정수 n을 스택에 삽입
        stack.append(command[1])
    elif command[0] == "pop": #스택에서 가장 위 정수를 빼고 그 수를 출력, 정수 없으면 -1 출력
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif command[0] == "size": #스택에 들어있는 정수의 개수 출력
        print(len(stack))
    elif command[0] == "empty": #스택이 비어있으면 1, 아니면 0 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top": #스택의 가장 위에 있는 정수 출력, 없는 경우엔 -1
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])