import sys

N, K = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort(reverse=True) #내림차순으로 정렬(큰 값이 앞으로)

cnt = 0
for coin in A:
    if K >= coin:
        cnt += K//coin
        K = K % coin
        if K<=0:
            break

print(cnt)

# cnt = 0

# for i in range(N-1, 0, -1):
#     cnt += K//A[i]
#     K=K%A[i]

# print(cnt)