T = int(input())

for i in range(T):
    P = []
    R, S = input().split()
    S = list(S)
    for i in range(len(S)):
        P.append(S[i]*int(R))
    print(''.join(P))


# #T = 테스트 케이스 개수
# #S = 문자열
# #R = 각 문자열을 R번 반복해서
# #P= S 문자열 속 문자를 각각 R번씩 반복해 새로 만든 문자열

# T = int(input())

# if T>=1 and T<=1000:
#     for i in range(T):
#         S_list=[]
#         P_list=[]
#         str = input()
#         R, S = str.split(" ")
#         R = int(R)
#         if S>=1 and S<=20:
#             if R>=1 and R<=8:
#                 S_list=list(S)
#                 for i in range(0, len(S_list)):
#                     P_list.append(S_list[i]*R)
#                 print(''.join(P_list)) #리스트 요소들을 합치는 Join 함수 -> '구분자'.Join(리스트))
    
        