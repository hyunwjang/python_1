#원화를 입력, 환율 입력 -> 달러값

won = input('원화를 입력 주세요')
dollor = input('환율을 입력 주세여')

try:#예외가 발생 할 수 있는 코드
    print(int(won) / int(dollor))
except ValueError as e:#예외가 발생할때 실행할 코드
    print('문자열 잘못 입력 하였습니다.',e)
except ZeroDivisionError as e:
    print('0은 나눌수 없습ㄴ디ㅏ.',e)
else:
    print('예외가 발생하지 않았을때 실행되는 코드')
finally:#리소스를 반환을 꼭 해야되는 경우
    print('예외가 발생하던지 않던지 항상 실행되는 코드')
    
print("프로그램이 끝났습니다.")