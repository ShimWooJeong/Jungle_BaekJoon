N = int(input())

N_list = []
for i in range(N):
    N_list.append(int(input()))

N_list.sort()

for i in range(len(N_list)):
    print(N_list[i])