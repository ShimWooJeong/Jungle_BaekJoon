import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    grade = [] #성적 담을 배열
    cnt = 1 #채용 수, 서류 1등은 무조건 채용 = 1로 초기화
    for _ in range(N):
        d_grade, i_grade = map(int, sys.stdin.readline().split())
        grade.append((d_grade, i_grade))
    grade.sort() #서류 심사를 기준으로 오름차순 정렬
    front = grade[0][1] #서류 심사 1등한 지원자의 면접 등수

    for i in range(1, N): #서류 2등부터 끝까지
        if grade[i][1] == 1: #면접 1등자가 나오면 게임 끝
            cnt+=1 #어차피 그 뒤 지원자들은 서류 점수도, 면접 점수도 해당 지원자보다 떨어지게 됨
            front=grade[i][1] #cnt+=1 해주고 front도 면접 1등 지원자로 초기화 해준 후 break 끝냄
            break
        if front > grade[i][1]: #채용된 앞에 지원자보다 면접 등수가 더 높다면(그니까 값이 더 작은)
            cnt+=1 #채용하고
            front=grade[i][1] #면접 등수 갱신
    print(cnt)