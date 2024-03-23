def move(n:int, x:int, y:int):
    middle = 6-x-y
    if n>1:
        move(n-1, x, middle)
    print(x, y)

    if n>1:
        move(n-1, middle, y)

num = int(input())

print(2**num-1)

if num<=20:
    move(num, 1, 3)