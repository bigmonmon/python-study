""" [연습]
    함수 정의 : count_words
    인자 : filename

    인자로 받은 파일명을 open 하여 파일을 읽어서 단어를 수를 출력한다.
    존재하지 않는 파일명으로 예외가 발생해도 아무런 일을 하지 않는다
"""
def count_words(filename):
    fname = './data/'+filename
    try:
        with open(fname, 'rt', encoding='utf-8') as f:
            context = f.read()
    except FileNotFoundError as e:
        pass
    else:
        result = len(context.split())
        print(filename, '>', result, '개')

# 존재하지 않는 파일명도 있음
filenames = ['sample.xml', 'xxxx.xxx', 'temp.json']
for filename in filenames:
    count_words(filename)