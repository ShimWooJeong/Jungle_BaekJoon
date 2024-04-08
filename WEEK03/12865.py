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