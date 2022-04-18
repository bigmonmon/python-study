"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = -1
if a :
    print('True')
else:
    print('False')

if not a :
    print('True2')

# ------------------------------------
a = 10
b = -1

if a and b:
    print('True3')

if a or b:
    print('True4')

print(a and b)  # and는 뒤의 값까지 기다려야해서 b가 결정 값이다
print(a or b)   # or은 앞에 값이 true이면 실행되므로 처음에 true값이 되는 값이 결정 값이다.

# --------------------------------------
a = 100
if a:
    print('A')
    print('B')
    print('C')

# ---------------------------------------
a = 10
b = -1

if a:
    c = 2
elif b:
    c = 4
else:
    c = 6
print(c) # 2