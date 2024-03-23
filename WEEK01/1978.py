#주어진 수 N개 중 소수가 몇 개인지 출력
#N: 수의 개수<=100
#N개의 수<=1,000
#본인보다 작은 숫자로 나눠보면서 만약 나누어 떨어진다(나머지가 0이다) = 소수가 아님
def isDecimal(num:int):
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0: #나누어 떨어지지 않으면 소수
            cnt+=1
    if cnt==1:
        return True
    else:
        return False

N = int(input())
num_list=list(map(int, input().split()))
sum=0

for i in range(len(num_list)):
    if isDecimal(num_list[i])==True:
        sum+=1

print(sum)