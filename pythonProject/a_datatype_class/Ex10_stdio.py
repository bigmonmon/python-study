"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""


#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
#name = input("이름을 입력하세요 : ")
#print('당신의 이름은 ', name, '입니다')
# format() 이용
#print('당신의 이름은 {name} 입니다'.format(name=name))
# % 이용
#print('당신의 이름은 %s 입니다' % (name))

#---------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력 -> eval() 이용
#age = input('나이를 입력하세요')
#print('당신의 나이는', eval(age)+1, '입니다.')

#
print('친구'+'안녕')
print('친구','안녕')
print('친구''안녕')

#----------------------------------
# 단을 입력받아 구구단을 구하기
#num = input('몇 단을 보시겠습니까?')
#for i in range(1,10):
#    print(num, '*' , i, '=', eval(num)*i, end=', ' if i < 9 else '')

#-----------------------------------------
# print() 함수



# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3

# -------------------------------------------------------
# 1.
#num = []
#sum = 0
#for i in range(5):
#    innum = input('정수를 입력하세요 : ')
#    num.append(innum)
#    sum += eval(num[i])
#print('평균 = ',sum/5)

# 2
instr = input('문자열 입력 : ')
reverse_name = ''
for c in instr:
    reverse_name = c + reverse_name
print('결과 : ',reverse_name)


