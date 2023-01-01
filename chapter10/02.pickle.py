# 1. 파이썬 객체를 pickle로 저장하기 

import pickle

data = { 
        '목표 1 ': '매일 팔굽혀 펴기 100호',
        '목표 2 ': '매일 코딩공부 1시간'
        }


file  = open('./myvenv/chapter10/data.pickle','wb')

pickle.dump(data,file)
file.close()


# 2. pickle 파일 파이썬으로 가져오기 

file  = open('./myvenv/chapter10/data.pickle','rb')
data = pickle.load(file)
print(data)
file.close()
