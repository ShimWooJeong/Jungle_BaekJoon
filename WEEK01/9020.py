import sys

def isDecimal(num:int): #소수 판별 함수
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0: #나누어 떨어지지 않으면 소수
            cnt+=1
    if cnt==1:
        return True
    else:
        return False

def Decimal_list(num:int): #소수 리스트 뽑는 함수
    de_list=[]
    for i in range(2, num):
        if isDecimal(i) == True:
            de_list.append(i)
    return de_list

def gold_partition(num:int, de_list:list): #최소 차이 소수 조합 찾기
    x = num//2
    y = num//2
    for i in range(num//2):
        if x in de_list and y in de_list:
            print(x, y)
            break
        else:
            #print(x, y)
            x-=1
            y+=1

T = int(sys.stdin.readline())
n_list=[]

for i in range(T):
    n_list.append(int(sys.stdin.readline()))

de_list = Decimal_list(max(n_list))

for i in range(len(n_list)):
    gold_partition(n_list[i], de_list)


