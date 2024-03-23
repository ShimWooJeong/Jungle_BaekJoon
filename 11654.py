#알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램

str = input()

if type(str) == int:
    if str>=0 and str<10:
        print(ord(str))
else:
    print(ord(str))

#ord() -> 글자를 아스키코드로
#chr() -> 아스키코드를 글자로