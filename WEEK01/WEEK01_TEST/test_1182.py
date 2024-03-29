import sys
N, S = map(int, input().split())
cnt = 0
num_list = list(map(int, input().split()))
result = []

def cNr(start):
    global cnt
    if sum(result) == S and len(result) > 0 :
        cnt += 1

    for i in range(start, N):
        #print(f'num_list[{i}]: ', num_list[i])
        result.append(num_list[i])
        #print('result: ', result)
        cNr(i+1)
        #재귀 호출로 각 원소의 선택 여부를 결정한다.
        #부분 집합에 새로운 원소가 추가되고, 원소 포함 여부에 따라 새로운 부분집합 생성
        result.pop()
        #재귀가 종료된 후 마지막으로 추가된 원소를 제거함으로써 이전 상태로 돌아감 = 백트래킹
        #print('pop_result: ', result)

cNr(0)
print(cnt)

