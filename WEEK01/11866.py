N, K = map(int, input().split())

queue = []
for i in range(1, N+1):
    queue.append(i)
yosep = []
#for i in range(N):
while len(queue) != 0: # queue가 빌 때까지 반복
    for i in range(K-1):
        queue.append(queue.pop(0)) # K-1개를 큐의 앞에서 pop해서 뒤로 append 해줌
    yosep.append(queue.pop(0)) #K번 째가 될 때 yosep에 pop

print("<", ", ".join(map(str, yosep)), ">", sep="")

# join함수: 배열을 문자열로 묶을 수 있음
# join함수를 쓰려면 str형으로 변환해줘야 함