msg = '행복해'            # 문자열
li = ['a','b','c']      # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking : 요소분해
c1, c2, c3 = msg
print(c1)   # msg 변수 대신 li, tpl, di
print(c2)
print(c3)

alist = [(1,2),(3,4),(5,6)]

# 출력 양식 : 1 + 2 = 3
for i, j in alist:
    print('{} + {} = {}'.format(i, j, i+j))

# (2) enumerate() 함수 : 각 요소와 인덱스를 같이 붙여주는 함수
user_list = ['개발자', '코더', '프로그래머', '분석가']
for value in user_list:
    print(value)

for value in enumerate(user_list):      # enumerate = 튜플로 인덱스번호를 붙여서 출력한다.
    print(value)

for idx, value in enumerate(user_list):
    print(idx, ':', value)

# (3) zip()
days = ['월', '화', '수']
doit = ['잠자기', '놀기', '밥먹기', '공부']

print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for d, hail in zip(days, doit):
    print(d,'요일에 할일 : ', hail)

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2','b3']
for a, b in zip(alist, blist):
    print(a, b)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))


