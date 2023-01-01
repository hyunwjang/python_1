import csv
file = open('./myvenv/chapter10/student.csv', 'r', newline ="", encoding = 'utf-8-sig')

reder = csv.reader(file)


for data in reder:
    print(data)
    
file.close()