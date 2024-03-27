import sys
import heapq

N = int(sys.stdin.readline())

left_heap = [] #최대 힙
right_heap = [] #최소 힙

for i in range(N):
    x = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)

    if  len(right_heap) > 0 and -left_heap[0] > right_heap[0]:
        # len(right_heap)>0 말고 그냥 right_heap이라고만 적어도 비어있지 않은 상태라는 의미
        temp1 = -heapq.heappop(left_heap)
        temp2 = heapq.heappop(right_heap)
        heapq.heappush(right_heap, temp1)
        heapq.heappush(left_heap, -temp2) # 최소힙에서 최소힙으로 넣어주는거니까 음수화
    print(-left_heap[0])

    # 틀렸다고 뜬 코드:
    # 그러니까 right_heap의 최솟값과 left_heap의 최댓값을 비교했을 때
    # left_heap의 크기가 더 크면 안 됨
    # 왜냐면 left는 중간값보다 작고 right는 중간값보다 큰 게 전제조건이니까
    # 그러니까 이런 경우 둘의 값을 swap 해줘야 함
    # 그런데 이 조건은 right_heap이 이 비어있지 않을 때에 따져볼 수 있음
    # if len(left_heap) > len(right_heap)+1:
    #     temp = -heapq.heappop(left_heap)
    #     heapq.heappush(right_heap, temp)
    # elif len(left_heap) < len(right_heap):
    #     temp = heapq.heappop(right_heap)
    #     heapq.heappush(left_heap, temp)
    
# 노가다 뜬 코드 -> 시간 초과
# heap = []
# for i in range(1, N+1):
#     temp = []
#     temp2 = []
#     num = int(sys.stdin.readline())
#     heapq.heappush(heap, num)

#     if i==1:
#         temp.append(heapq.heappop(heap))
#         print(temp[0])
#         heapq.heappush(heap, temp[0])
#         temp.clear()
#     elif i==2:
#         for i in range(2):
#             temp.append(heapq.heappop(heap))
#         if temp[0] > temp[1]:
#             print(temp[1])
#         else:
#             print(temp[0])
#         for j in range(2):
#             heapq.heappush(heap, temp[j])
#         temp.clear()
#     else:
#         if abs(i%2==1): #홀수면
#             for j in range(i//2+1):
#                 temp.append(heapq.heappop(heap))
#             print(temp[i//2])
#             for j in range(len(temp)):
#                 heapq.heappush(heap, temp[j])
#             temp.clear()
#         elif abs(i%2==0): #짝수면
#             for j in range(i//2+1):
#                 temp.append(heapq.heappop(heap))
#             a = temp[i//2-1]
#             b = temp[i//2]
#             if a > b:
#                 print(b)
#             else:
#                 print(a)
#             for j in range(i//2+1):
#                 heapq.heappush(heap, temp[j])
#             temp.clear()
