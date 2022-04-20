pin = '880122-1234567'
birthday = "홍길동님 생년월일 : "+pin[0:6]
if pin[7:8] == '1':
    gender = '성별 : 남자'
else:
    gender = '성별 : 여자'

print(birthday)
print(gender)


a = [1,3,4,5,2]
a.sort()
a.reverse()
print(a)

a = ['독도는', '대한민국의', '아름다운', '섬입니다']
result = " ".join(a)
print(result)

a = (1,2,3)
a = a + (4,)
print(a)

kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]
midterm_score = [kor_score, math_score, eng_score]

first_sum = 0
second_sum = 0
third_sum = 0
fourth_sum = 0
fifth_sum = 0

for i in range(len(kor_score)):
    for j in range(len(midterm_score)):
        if(i == 0):
            first_sum += midterm_score[j][i]
        elif(i == 1):
            second_sum += midterm_score[j][i]
        elif (i == 2):
            third_sum += midterm_score[j][i]
        elif (i == 3):
            fourth_sum += midterm_score[j][i]
        elif (i == 4):
            fifth_sum += midterm_score[j][i]

print('첫번째 학생 총합 :', first_sum, '평균 :', first_sum/len(midterm_score))
print('두번째 학생 총합 :', second_sum, '평균 :', second_sum/len(midterm_score))
print('세번째 학생 총합 :', third_sum, '평균 :', third_sum/len(midterm_score))
print('네번째 학생 총합 :', fourth_sum, '평균 :', fourth_sum/len(midterm_score))
print('다섯번째 학생 총합 :', fifth_sum, '평균 :', fifth_sum/len(midterm_score))


life = {'animal':{'cats':{'Kim':'', 'Lee':'', 'Choi':''}, 'octopi':'', 'emus':''}, 'plants':'', 'other':''}

print(life)

for i in range(3):

    try:

        print(i, 3// i)

    except ZeroDivisionError:

        print("Not divided by 0")


