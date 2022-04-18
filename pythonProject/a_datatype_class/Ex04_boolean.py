# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사


hungry = True
sleepy = False
print(type(hungry)) #<class 'bool'>
print(not hungry)   #False
print(hungry and sleepy)  #False
print(hungry or sleepy)  #True
print(hungry & sleepy)  #False
print(hungry | sleepy)  #True


"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False

"""

if('아'):
    print('True')   #True
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2') #False2
# *******************
# 행은 0번째 인덱스여서 False이다
msg = '행복합시다'
if(msg.find('행')):
    print('True3')
else:
    print('False3')

# ********************
# 가는 없는 글자니깐 -1값이 나온다 그래서 True이다
msg = '행복합시다'
if(msg.find('가')):
    print('True4')
else:
    print('False4')
