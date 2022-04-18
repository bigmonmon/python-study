"""
    [정리]

    * 함수 : 파일 내에서 일정한 작업을 수행하는 코드 블록
    * 모듈 : 함수나 클래스들의 파일
            모듈이름은 py 확장자를 제외한 파일 이름
    * 패키지 : 여러 모듈들을 모아놓은 디렉토리
            패키지 = 디렉토리
            모듈 = 파일

    [ 모듈 ]
    - 자주 사용되는 함수를 매번 작성하지 않고 하나의 모듈로 사용하여 재사용
    - 모듈 단위로 분리하여 설계함으로 작업의 효율을 높임
    - 동일한 함수나 클래스를 모듈로 관리

        ` 표준 모듈 : 파이썬 안에 기본적으로 제공하는 모듈
        ` 사용자 정의 모듈 : 개발자가 직접 정의한 모듈
"""
from random import choice

def get_weather():
    today = ['맑음','비','눈','폭우','돌풍','따뜻']
    return choice(today)

def get_date():
    today = ['월','화','수','목','금','토','일ㄴ']
    return choice(today)

if __name__=="__main__":

    print(get_date())
    print(get_weather())