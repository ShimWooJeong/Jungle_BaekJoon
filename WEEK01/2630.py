def cut(x:int, y:int, n:int):
    global white, blue # 전역변수
    color = paper[x][y] # 종이 색

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]: # 색종이의 [i][j]값들 중 color와 동일하지 않은 경우 재귀로 색종이 나눠주기
                cut(x+n//2, y, n//2)
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
            
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input()) # 한 변의 길이, 2^k = 2, 4, 8 ... 128 중 하나

paper = []
white = 0 # 흰색 색종이 개수
blue = 0 # 파란색 색종이 개수

for i in range(N):
    paper.append(list(map(int, input().split())))

cut(0, 0, N)

print(white)
print(blue)
