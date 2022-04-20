import json

f = open('./data/temp.json', 'rt', encoding='utf-8')
data = f.read()
print(data)

print('-'*100)
items = json.loads(data)
print(items)
print('-'*100)

print(type(data))
print(type(items))

for k, n in items.items():
    print(k,':',n, '>>', n['Job'])