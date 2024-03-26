import sys
import heapq

N = int(input())

heap = []
for i in range(1, N+1):
    temp = []
    temp2 = []
    num = int(input())
    print('num: ', num)
    heapq.heappush(heap, num)

    if i==1:
        temp.append(heapq.heappop(heap))
        print('-', temp[0])
        heapq.heappush(heap, temp[0])
        temp.clear()
    elif i==2:
        for i in range(2):
            temp.append(heapq.heappop(heap))
        if temp[0] > temp[1]:
            print('-', temp[1])
            for i in range(2):
                heapq.heappush(heap, temp[i])
            temp.clear()
        else:
            print('-', temp[0])
            for i in range(2):
                heapq.heappush(heap, temp[i])
            temp.clear()
    else:
        if i%2==1: #홀수면
            for i in range(N//2):
                temp.append(heapq.heappop(heap))
            print('-', heapq.heappop(heap))
            for i in range(N//2):
                heapq.heappush(heap, temp[i])
                temp.clear()
        else: #짝수면
            for i in range(N//2-1):
                temp.append(heapq.heappop(heap))
            for i in range(2):
                temp2.append((heapq.heappop(heap)))
            if temp2[0] > temp2[1]:
                print('-', temp2[1])
            else:
                print('-', temp2[0])
            for i in range(N//2-1):
                heapq.heappush(heap, temp[i])
                temp.clear()
            

