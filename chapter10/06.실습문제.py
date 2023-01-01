import csv

def show_profit(data):
    name = data[0]
    purchase_price = int(data[1])
    amount = int(data[2])
    target_price = int(data[3])
    
    profit = (target_price - purchase_price) * amount #수익금
    profit_ration =(target_price /purchase_price - 1) *100 #수익률
    
    print(f'수익금 {profit}, 수익률 {profit_ration:.2f}%')

data = [
    ['종목', '매입가', '수량','목표가'],
    ['삼성전자', 85000, 10, 90000]
    ,['naver', 380000, 4, 400000]
]

file = open('./myvenv/chapter10/mystock.csv', 'w', newline ="", encoding = 'utf-8-sig')
wrtier = csv.writer(file)

for d in data:
    wrtier.writerow(d)
    
file.close()


file = open('./myvenv/chapter10/mystock.csv', 'r', newline ="", encoding = 'utf-8-sig')

reader = list(csv.reader(file))

for data in reader[1:]:
    show_profit(data)
    # print(data)
    
file.close()
