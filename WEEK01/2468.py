import sys
from copy import deepcopy

def dfs(x:int, y:int, rain_area:list):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if rain_area[x][y] != 0: #안 잠겼다면
        rain_area[x][y] = 0 #방문했다는 의미
        dfs(x-1, y, rain_area)
        dfs(x, y-1, rain_area)
        dfs(x+1, y, rain_area)
        dfs(x, y+1, rain_area)
        return True
    return False
# max_value = max(map(max, areas)) #map함수로 2차원 배열에서 최대값 구하기

def find_max(areas:list, rain: int):
    temp = deepcopy(areas)
    sum=0
    for i in range(N):
        for j in range(N):
                if temp[i][j] <= rain:
                    temp[i][j] = 0
    #print(f'{rain}일 때: ', temp)
    for i in range(N):
        for j in range(N):
            if dfs(i, j, temp) == True:
                sum += 1
    return sum


def input_rain(areas: list):
    max_value = max(map(max, areas)) #map함수로 2차원 배열에서 최대값 구하기
    result = []
    for i in range(1, max_value): #비를 1~가장 높은 지역-1까지 넣어봄
        result.append(find_max(areas, i))
    return max(result)

N = int(sys.stdin.readline())
areas = []
for _ in range(N):
    areas.append(list(map(int, sys.stdin.readline().split())))

# for i in range(N):
#     for j in range(N):
#         if areas[i][j] <= 4: #비가 4만큼 온다고 가정
#             areas[i][j] = 0 #잠긴 애들 = 0
#rain = int(input())
# print('총 개수: ', find_max(areas, rain))       
print(input_rain(areas))
