"""
#----------------------------------------------------------
[튜플 자료형]
    1- 리스트와 유사하지만 튜플은 값을 변경 못한다.
    2- 각 값에 대해 인덱스가 부여
    3- 변경 불가능 (*****)
    4- 소괄호 () 사용

    - List : []
    - set : {}
    - tuple : ()
"""


# (1) 튜플 생성
print('------------------- 1. 튜플 생성-----------------')

t = ( 1, 2, 3)
print(t)
print(type(t))
print(t[0])


# (2) 튜플은 요소를 변경하거나 삭제 안됨
# t[1] = 0
# del t[1]
print('------------------- 2 -----------------')


# (3) 하나의 요소를 가진 튜플
print('------------------- 3 -----------------')

t3 = (1,)     # 하나의 요소를 가지고 있는 튜플은 뒤에 ,를 꼭 찍어 줘야 한다
print(t3)
print(t3[0])
print(type(t3))


# (4) 인덱싱과 연산자
print('------------------- 4 -----------------')

t = ('하나', '둘', '셋')
print(t[-1])
print(t[1:])
print( t + t3)
print( t * 3 )

a, b, c = t
print(a)
print(c)