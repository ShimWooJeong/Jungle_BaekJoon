import sys

N = int(sys.stdin.readline())

tower_height = list(map(int, sys.stdin.readline().split()))
tower_list = []
answer = []
stack = []
for i in range(N):
    tower_list.append([tower_height[i], i+1]) # i+1인 이유: 타워번호 = index+1

for i in range(N):
    while stack: #stack에 값이 있는 동안 실행
        # 여기서 stack에 있는 타워 높이와 판단할 tower_list의 타워 길이를 비교
        if stack[-1][0] <= tower_list[i][0]:
            # 높이가 같아도 실행하는 이유는 높이가 같아도 index,
            # 즉 타워 번호를 최신화 시켜줘야 하기 때문
            stack.pop()
            #그 전에 스택에 놓였던 타워보다 현재 타워가 높다면
            #그 전 타워 pop하고 높은 타워를 stack에 push(27번 째 line)
        elif stack[-1][0] > tower_list[i][0]:
            answer.append(stack[-1][1])
            # 현재 타워보다 stack의 타워가 더 크면 stack의 타워 높이는 answer에 push
            break
    if not stack:
        answer.append(0)
    stack.append(tower_list[i]) # 이 코드로 인해 다음 타워를 계속해서 탐구하게 됨

print(" ".join(map(str, answer)), sep="")


