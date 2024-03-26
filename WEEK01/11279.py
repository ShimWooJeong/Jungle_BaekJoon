import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap)) #음수화 했기 때문에 다시 양수화 해줌
    else:
        heapq.heappush(heap, -x) #최대 힙을 적용시키기 위해 음수화 시킴

#최대 힙을 활용하지 않으면 시간 초과 문제 발생