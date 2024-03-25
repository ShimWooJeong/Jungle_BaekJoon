#자료를 오름차순으로 정렬
#자료의 Middle 값이 찾고자 하는 Taget인 지 비교
#Middle!=Target인 경우 대소관계를 비교해 탐색 범위를 좁히고
#Middle==Target일 때까지 반복
#Target<Middle -> end를 Middle 왼쪽 값으로 바꿔줌(절반 왼쪽 탐색)
#Target>Middle -> start를 Middle 오른쪽 값으로 바꿔줌(절반 오른쪽 탐색)

def binary_search(target:int, data:list):
    #target(찾아내고 싶은 값)=M[i], data(탐색할 장소)=A[]
    #data.sort() 함수 호출마다 정렬하면 안 됨
    start = 0
    end = len(data)-1
    while start<=end: #start>=end면 탐색이 끝남
        mid = (start+end)//2
        if data[mid] == target: #일치, 찾음
            return 1
        else:
            if data[mid] > target: #찾고자 하는 값<중간 값 end=mid-1로 왼쪽 탐색만)
                end=mid-1
            elif data[mid] < target: #찾고자 하는 값>중간 값이니까 start=mid+1로 오른쪽 탐색만
                start=mid+1
    return 0 #못 찾음


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

for i in range(M):
    print(binary_search(B[i], A))


# for i in range(M):
#     if B[i] in A:
#         print(1)
#     else:
#         print(0)