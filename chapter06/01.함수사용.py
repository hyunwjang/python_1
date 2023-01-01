# def print_m(name, data):
#     print('안녕하세요',name,'님')
#     print('현재 프리엄 서비스 사용기간이 ', data,'일 남았습니다.')
    
# print_m('장현우', 3)

# import random

# def getgame():
#     num = random.randint(1,10)
#     return num
# # print(getgame())


# print_m('장현우', getgame())

import random
lotto = []
# for i in range(6):
#     lot = random.randint(1,45)
#     lotto.append(lot)
    
# print(set(lotto))


count = 0
while True:
    if count >=6:
        break
    lot = random.randint(1,46)
    if lot not in lotto:
        lotto.append(lot)
        count += 1
    

lotto.sort()
print(lotto)
