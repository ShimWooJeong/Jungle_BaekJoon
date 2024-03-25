def Trees_cut(M:int, Trees:list):
    start=0
    end=max(Trees)
    #오른쪽 끝 index 위치가 아닌, 최댓값
    #이 문제는 list 내 특정 요소를 찾는게 아닌, 범위 내에서 적용될 수 있는 최댓값을 구하는 문제니까
    #end를 len(Trees)-1로 두는 것이 아닌 최댓값으로 두는 것 같음
    #이진 탐색의 핵심은 검색 공간을 절반씩 줄여나가는 것
    #꼭 리스트를 절반으로 나눈다는 생각을 하지 않아도 된다!!

    while start<=end:
        mid = (start+end)//2 #절단기 설정 높이 = 최댓값과 최솟값의 평균
        sum = 0 # 자른 나무 길이의 Total
        for i in Trees:
            if i > mid:
                sum += i-mid

        if sum >= M:
            # 자른 나무 길이가 목표값보다 같거나 크다면 높이를 높여야 함
            # 왜 같은 경우도 포함하는지? 우리가 구하는 건 최댓값이기 때문에
            # 잘라진 나무가 충분하다면(같거나 크다면) 최대한 나무 길이를 살리기 위해 한 번 더 시도
            # 즉 평균 값이 높아져야 하니까 start가 높아져야 함
            start=mid+1
        else: # sum < M
            # 자른 나무 길이가 목표값보다 부족하다면 높이를 낮춤
            # 즉 평균 값이 낮아져야 하니까 end가 낮아져야 함
            end=mid-1
    return end
            
N, M = map(int, input().split())
Trees = []

Trees = list(map(int, input().split()))
Trees.sort()
print(Trees_cut(M, Trees))