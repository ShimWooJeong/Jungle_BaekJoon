def quick_sort(A:list, left:int, right:int):
    pivot = A[(left+right)//2] # pivot 가운데 Index로 설정
    pl, pr = left, right # 왼쪽 커서과 오른쪽 커서

    while pl <= pr:
        while A[pl] < pivot: # 왼쪽 집합에서 pivot 값보다 작은 값을 찾을 때까지 탐색
            pl += 1
        while A[pr] > pivot: # 오른쪽 집합에서 pivot 값보다 큰 값을 찾을 때까지 탐색
            pr -= 1
        if pl <= pr: # 왼쪽 커서와 오른쪽 커서 모두 값을 찾은 상태에서 pl<=pr을 만족하는지
            #만약 조건에 만족한다면 둘의 값을 교환하고 다시 탐색하도록 +, -
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
    
    if left < pr: # while문을 돌았는데도 pr이 왼쪽 끝에 도달하지 못 했다면 해당 범위 재정렬
        quick_sort(A, left, pr)
    if pl < right: # while문을 돌았는데도 pl이 오른쪽 끝에 도달하지 못 했다면 해당 범위 재정렬
        quick_sort(A, pl, right)

num = int(input('원소 수: '))
x = []

for i in range(num):
    x.append(int(input()))

print(x)
quick_sort(x, 0, len(x)-1)

print('정렬 후: ', x)
    
