# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서(인덱스)를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
s = {}                  # 빈 dictionary 임
s = set([1,2,3,1,1])
print(s)    # s = {1,2,3}

b = {3,4,5,6}

print(s.intersection(b))
print(s.union(b))

print( s | b )
print( s & b )

print( s - b )
print( b - s )



