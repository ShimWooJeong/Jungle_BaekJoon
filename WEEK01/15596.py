def solve(a: list)->int:
    ans = 0
    for i in range(len(a)):
        ans+=a[i]
    return ans
    
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
print(solve(a))

#a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
#return:a에 포함되어 있는 정수 n개의 합(정수)