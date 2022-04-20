"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다
"""
'''
try:
    f = open('./data/data.txt', 'rt', encoding='utf-8')
except FileNotFoundError as e:
    print('해당 파일이 존재하지 않습니다.')
else:
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
finally:
    print('프로그램 종료')
'''

'''
f = open('./data/data.txt', 'rt', encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''

with open('./data/data.txt', 'rt', encoding='utf-8') as f:      #with 구문을 쓰면 자동 close가 된다
    while True:
        line = f.readline()
        if not line: break
        print(line)

# data.txt 파일에서 읽어서 전체 단어수를 구해서 출력
# content = f.read()

#글자수 세기
with open('./data/data.txt', 'rt', encoding='utf-8') as f:      #with 구문을 쓰면 자동 close가 된다
    context = list(f.read())
    for i in context:
        if i == '\n':
            context.remove(i)
    print(len(context))

try:
    with open('./data/data.txt', 'rt', encoding='utf-8') as f:
        context = f.read()
except FileNotFoundError as e:
    print('해당 파일이 존재하지 않습니다.')
else:
    result = len(context.split())
    print(result, '개')
finally:
    print('프로그램 종료')