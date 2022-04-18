"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""

'''
[자바의 경우]
class Sample {
    String data = "Hello";
    String name;
    public Samole(String name){
        this.name = name;
    }
}
'''

class Sample:
    data = 'Hello'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('객체 생성')

    def __del__(self):
        print('객체 소멸')

s = Sample("홍길동", 25)
print(s.data)
print(s.name)
print(s.age)
print(dir(s))
del s





"""
    1) 인스턴스와 클래스 변수
        클래스 변수 : 클래스명.변수        (자바에서는 static)
        인스턴스 변수 : 인스턴스명.변수
        
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
"""

class Book:
    cnt = 0
    def __init__(self, title):
        self.title = title
        self.cnt += 1

    def output(self):
        print(self.cnt, self.title)

b1 = Book('행복')
b2 = Book('먹고 살자')

b1.output()
b2.output()


'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''


