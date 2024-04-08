def knapsack():
    n, k = [int(x) for x in input().split()] #n: 물건 개수, k: 가방 무게
    table = [0] * (k+1) #테이블 세팅
    for _ in range(n):
        w, v = [int(x) for x in input().split()] #w: 무게, v: 가치
        for j in range(k, 0, -1):
            if j+w <= k and table[j] != 0: #테이블 범위 안에 있어야 하고, 값이 0이 아닐 때
                table[j+w] = max(table[j+w], table[j] + v)
        table[w] = max(table[w], v)
    print(max(table))

#점화식: table[i][j+w[i]]=max(table[i-1][j+w[i]], table[i-1][j]+v[i])
                            #기존의 값            #새로운 값
#knapsack()

def knapsack2():
    n, k = map(int, input().split())
    object_list = [[0, 0]]
    for _ in range(n):
        object_list.append(list(map(int, input().split())))
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            weight = object_list[i][0]
            value = object_list[i][1]
            if j < weight: #가방에 넣을 수 없음 (j = 가방 남은 공간, weight = 물건 무게)
                dp[i][j] = dp[i-1][j] #위에 값 그대로 가져오기
            else: # 가방에 넣을 수 있음
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
    print(dp[n][k])

knapsack2()