origin_pass = '1234'
input_pass = input('비밀번호르 입력 바랍니다.')

if input_pass == origin_pass:
    print('로그인 성공')
elif input_pass != origin_pass:
    print('로그인 실패')