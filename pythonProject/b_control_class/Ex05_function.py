"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

# (1) 인자도 없고 리턴값도 없는 함수
def func():
    print('inside func')

func()
result = func()
print('result = ', result)  # 리턴값이 없으면 None

# return값 있는 경우
def func():
    print('inside func')
    return 'hello'

func()
result = func()
print('result = ', result)

# (2) 리턴값이 여러개인 경우
def func(arg):
    return arg+5, arg-5

result = func(10)
print(result)   #리턴값이 여러개면 튜플로 리턴이 하나다

add, minus = func(10)
print('add =', add)
print('minus = ', minus)

# (3) 위치 인자 ( positional argument )
def func(greeting, name):
    print( greeting, '!!!!', name, '님')

func('안녕하세요', '홍길동')    #매개변수 순서로 들어간다 -> 위치인자
func('마이클', '하이')

# (4) 키워드 인자 (keyword argument)
func(name='마이클', greeting='하이') #순서가 헷갈릴때는 명확하게 keyword를 주는게 좋다

# 매개변수 지정 ( 기본값 지정 )
def func(greeting, name='아무개'):
    print( greeting, '!!!!', name, '님')
func("안녕하세요", "홍길동")
func("올라")

# [참고]
def func(a, b, c=100):
    return a*2 + b*3 + c*4

print( func(c=1, b=2, a=3)) #16
print( func(1,2,3)) #20
print( func(1,2 ) ) #408










'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''
def func(a, b, c=0, *args): # 뭐가 들어올지 모르는 인자는 -> *args
    sum = a + b + c
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))   # args에 7,8,9가 튜플로 들어간다

# (6) 키워드 인자 모으기
def func(a, b, c=0, *args, **kwargs): #키워드 인자일 경우 -> **kwargs
    sum = a + b + c
    for i in args:
        sum += i
    for j in kwargs:
        sum += kwargs[j]
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))
print(func(4, 5, 6, 7, kor=80, eng=70))
print(func(4, 5, 6, 7, kor=80, eng=70, java=60))

def test(t):
	t = 20
	print ("In Function:", t)

x = 10
print ("Before:", x)
test(x)
print ("After:", x)

def sotring_function(list_value):
	return list_value.sort()

print(sotring_function([5,4,3,2,1]))

def is_yes(your_answer):
	if your_answer.upper() == "YES" or your_answer.upper() == "Y":
		result = your_answer.lower()

print(is_yes("Yes"))

'''
[ 연습문제 ]

- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수 ( 함수명 : even_filter )
    [ 실행 ]
        print(even_filter([1, 2, 4, 5, 8, 9, 10]))

- 주어진 수가 소수인지 아닌지 판단하는 함수 ( 함수명 : is_prime_number )
    [ 실행 ]
        print(is_prime_number(60))
        print(is_prime_number(61))

- 주어진 문자열에서 모음의 개수를 출력하는 함수 ( 함수명 : count_vowel )
    [ 실행 ]
        print(count_vowel("pythonian"))
'''

def even_filter(list):
    even = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even.append(list[i])
    return even
print(even_filter([1, 2, 4, 5, 8, 9, 10]))

def is_prime_number(num):
    for i in range(2 ,num):
        if num%i==0:
            return '소수가 아닙니다'
            break
    else:
        return '소수입니다'

print(is_prime_number(60))
print(is_prime_number(61))

def count_vowel(text):
    notext = ['a','e','i','o','u']
    return len([c for c in text if c in notext])
print(count_vowel("pythoniaaaan"))