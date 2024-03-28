N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

def quadTree(x, y, n):
    check_Pixel = graph[x][y]

    if n == 1: #픽셀 크기가 1인 경우
        print(graph[x][y], end='')
        return

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check_Pixel != graph[i][j]:
                #수학적으로 1,2,3,4분면 탐색이 아니라
                #왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
                #즉 2-1-3-4분면 순으로 재귀하기
                print("(", end='')
                quadTree(x, y, n//2) #왼쪽 위
                quadTree(x, y+n//2, n//2) #오른쪽 위
                quadTree(x+n//2, y, n//2) #왼쪽 아래
                quadTree(x+n//2, y+n//2, n//2) #오른쪽 아래
                print(")", end='')
                return
    
    print(graph[x][y], end='') #픽셀들이 모두 같은 색으로 칠해져 있는 경우
    return

quadTree(0, 0, N)



