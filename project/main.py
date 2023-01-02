import os
import csv
from post import Post
file_path = "./myvenv/project/data.csv"

#post 객체를 저장할 리스트
post_list =[]

#data.csv 파일이 있다면

if os.path.exists(file_path):
    #게시글 로딩
    print('게시글 로딩중')
    f = open(file_path, 'r', encoding='utf8')
    reader = csv.reader(f)
    for data in reader:
        #post 인스턴스 생성하기
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
else:
    #파일생성하기
    f = open(file_path, 'w', encoding= 'utf8', newline="")
    f.close()
    
    
#게시글쓰기
def write_post():
    '''게시글 쓰기'''
    print("\n\n -게시글 쓰기")
    title = input("제목을 입력해 주세요\n>>>")
    content = input("내용을 입력해주세요\n>>>")
    #글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("#게시물이 등록되었습니다.")
    
def list_post():
    """게시글 목록 함수"""
    id_list = []
    print("\n\n 게시글 목록")
    for post in post_list:
        print('번호 : ',post.get_id())
        print('제목 : ',post.get_title())
        print('조회수 : ',post.get_view_count())
        print("")
        id_list.append(post.get_id())
    while True:
        print('Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1를 입력해주세요)')
        try:                
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print('없는 글 번호 입니다.')
        except:
            print('숫자를 입력해주세요')
            
def detail_post(id):
    print('\n\n -게시글 상세 - ')
    
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            #조회수 증가
            print('번호 : ',post.get_id())
            print('제목 : ',post.get_title())
            print('본문 : ',post.get_countent())
            print('조회수 : ',post.get_view_count())
            taget_post = post
            
    while True:
        print("Q) 수정 : 1, 삭제 : 2(메뉴로 돌아가려면 -1을 입력)")
        
        try:
            choice = int(input(">>>"))
            if choice == 1:
                update_post(taget_post)
                break
            elif choice ==2:
                delete_post(taget_post)
                break
            elif choice ==3:
                break
            else:
                print('잘못입력하였습니다.')
        except:
            print('숫자를 입력하여 주세요')

#게시글 수정
def update_post(taget_post):
    """게시글 수정 함수"""
    print("\n\n -게시글 수정-")
    title = input("제목을 입력해 주세요\n >>>")
    content = input("본문을 입력해 주세요\n >>>")
    taget_post.set_post(taget_post.id, title, content, taget_post.view_count)
    print('#게시글이 수정되었습니다.')
    
#게시글 삭제
def delete_post(taget_post):
    post_list.remove(taget_post)
    
#게시글 저장
def save_post():
    f = open(file_path, 'w', encoding='utf8', newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_countent(), post.get_view_count()]
        writer.writerow(row)
        
while True:

    print("\n\n  - FASTCAMPUS BLOG -")
    print('메뉴를  선택해 주세요 ')
    print('1. 게시글 쓰기 ')
    print('2. 게시글 목록')
    print('3. 프로그램 종료')
    
    try:
        choice = int(input('>>>'))
    except ValueError:
        print('숫자를 입력하여 주시기 바랍니다.')
    else:
        if choice ==1:
            write_post()
        elif choice ==2:
            
            list_post()
        elif choice ==3:
            print("프로그램 종료")
            save_post()
            break