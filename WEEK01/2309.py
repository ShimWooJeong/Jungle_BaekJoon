height = [] # 아홉 난쟁이의 키
for i in range(9):
    height.append(int(input()))

height.sort()

x = [] # 2개씩 묶은 모든 조합
for i in range(8):
    for j in range(i+1, 9):
        x.append([height[i], height[j]])

y = []
for i in range(len(x)): # 아홉 난쟁이 키에서 모든 2개의 조합을 빼서 합=100인 조합 찾기
    y += height
    for j in range(2):
        y.remove(x[i][j])
    if sum(y) == 100:
        break
    else:
        y.clear()

for i in range(len(y)):
    print(y[i])