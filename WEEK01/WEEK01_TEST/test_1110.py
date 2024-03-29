N = int(input())
n = N
#while 문 안에서 N을 new 값으로 반복해서 갱신해주기 때문에
#본래 N값에 영향을 주지 않도록 따로 값을 저장해줄 변수 = n
cnt = 0

while True:
    ten = N // 10 #십의 자리 수
    num = N % 10 #일의 자리 수
    new = (num*10)+((ten+num)%10)
    cnt += 1
    if n == new:
        break
    N = new
print(cnt)
