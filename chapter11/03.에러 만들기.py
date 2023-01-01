#raise 구문을 사용해서 에러를 강제로 발생시켜 봅시다.

class positiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수를 입력 불가")
try:
    num = int(input('음수를 입력바랍니다.'))
    if num >= 0:
        raise positiveNumberError
except Exception as e:
    print('에러 발생!', e)