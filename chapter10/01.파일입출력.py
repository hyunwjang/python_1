#파일 만들기
# file = open('./myvenv/chapter10/data.txt', 'w', encoding = 'utf8')
# file.write('1.스타트코딩과 함께 하는 파이썬 공부')
# file.close


# #2. 파일 추가
# file = open('./myvenv/chapter10/data.txt', 'a', encoding = 'utf8')
# file.write('\n2. 비전공자도 정말 쉽게 배울 수 있습니다.')
# file.close

# 3. 파일 읽기
file = open('./myvenv/chapter10/data.txt', 'r', encoding = 'utf8')
#3.1 vkdlf wjscpdlfrrl
# data = file.read()
# print(data)
file.close

#3.1 파일 한줄읽기 
while True:
    
    data = file.readline()
    print(data,end ="")
    if data == "":
        break
    
file.close 