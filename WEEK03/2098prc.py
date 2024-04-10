import sys


def go(now, trace):
    if dp[now][trace]: #이미 계산된 값이 있다면, 이미 최소인 거니까 해당 값 반환
        return dp[now][trace]

    # 기저 조건
    if trace == (1 << N)-1: #모든 도시를 방문한 경우(1<<N)-1 = 1111 = 15, 1/2/3/4 도시 다 방문
        return path[now][0] if path[now][0] > 0 else MAX
    #다시 0으로 돌아갈 경로가 있다면 path[now][0] 반환, 아니면 MAX = 즉 그 경로는 다시 돌아갈 수 없으니 소용 없음

    # 각 상태에서 구해야하는 값
    cost = MAX
    for i in range(1, N): #0번 출발 도시기 때문에 1부터 탐색
        if not trace & (1 << i) and path[now][i]: #방문하지 않았고 이동할 경로가 있다면
            val = go(i, trace | (1 << i)) #i부터 나머지 도시로 갈 최소비용
            cost = min(cost, val+path[now][i]) #그 중 최솟값 갱신

    # dp에 값 갱신
    dp[now][trace] = cost
    return dp[now][trace]


N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
MAX = sys.maxsize

# print(dp)
print(go(0, 1))
print(*dp, sep='\n')