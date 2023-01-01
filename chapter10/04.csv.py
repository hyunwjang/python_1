import csv

data = [
    
    ['이름','반','번호']
    ,['재석, 1,20']
    ,['홍철, 2,22']
    ,['명수', 3,23]
]

file = open('./myvenv/chapter10/student.csv', 'w', newline ="", encoding = 'utf-8-sig')
wrtier = csv.writer(file)

for d in data:
    wrtier.writerow(d)
    
file.close()