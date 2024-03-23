import sys

N = int(sys.stdin.readline().strip())

N_list = []
for i in range(N):
    N_list.append(int(sys.stdin.readline().strip()))
    #readline 뒤에 '\n' 개행 문자 제거 .strip()

N_list.sort()

for i in range(N):
    print(N_list[i])