N = int(input())
words=[]

for i in range(N):
    word = str(input())
    if word not in words:
        words.append(word)

words.sort() #사전순 정렬
words.sort(key=len) #길이순 정렬

for i in range(len(words)):
    print(words[i])
    