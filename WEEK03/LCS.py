import sys

string_A = ' '+sys.stdin.readline().rstrip() #dp[0][j]일 때와 dp[i][j]일 때 padding값을 넣어주기 위해
string_B = ' '+sys.stdin.readline().rstrip() #문자열 앞에 빈 문자열을 추가해줘야 함

print(string_A)
print(string_B)

dp = [[0] * len(string_B) for _ in range(len(string_A))]
#0으로 채워진 dp 리스트 생성

for i in range(1, len(string_B)):
    for j in range(1, len(string_A)):
        if i==0 or j==0: #padding값 설정 부분인데, 사실 선언할 때 이미 0으로 채워지도록 리스트를 생성했기 때문에
            dp[i][j] = 0 #이 조건문은 필요하진 않음
        elif string_A[j] == string_B[i]: #문자열이 똑같다면
            dp[i][j] = dp[i-1][j-1]+1
        else: #문자열이 다르다면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
print(dp[-1][-1])
print()
print(*dp, sep='\n')
print(len(string_B), len(string_A))
result = []

def Back_Tracking(i, j):
    while dp[i][j] != 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            result.append(string_A[j])
            i -= 1
            j -= 1
    return result

print(Back_Tracking(len(string_B)-1, len(string_A)-1))