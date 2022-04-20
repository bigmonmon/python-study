# data/sample.json 파일을 읽어서 값의 총합을 구해서 출력

import json

f = open('./data/sample.json', 'rt', encoding='utf-8')
data = f.read()
items = json.loads(data)

total = 0
count = 0
for n in items.values():
    total += n['price']
    count += n['count']
print('총합 = ',total,' 총갯수 = ', count)


sum_price = 0
sum_cnt = 0
sum_price = sum(s['price'] for s in items.values())
sum_cnt = sum(s['count'] for s in items.values())

print("총합은 {}, 총 개수는 {}".format(sum_price,sum_cnt))
print('-'*50)


f = open('./data/sample.txt', 'rt', encoding='utf-8')
sum = 0
temp = []
while True:
    line = f.readline()
    if not line: break

print(sum)



