champion1_name = '이즈리얼'
champion1_health = 700
champion1_attack = 90


print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = '리신'
champion2_health = 800
champion2_attack = 95


print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")


def basic_attck(name , attack):
    print(f"{name} 기본공격 {attack}")
    
basic_attck(champion1_name, champion1_attack)
basic_attck(champion2_name, champion2_attack)

print('-'*20)

class Champion:
    def __init__(self, name, health, attack):
        #init 은 정보를 입력한다
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{self.name},기본공격{self.attack}")
    def basic_attack(self):
        #init의 받은 내용을 출력한다
        print(f"{self.name} 기본공격{self.attack}")
      
        
erzeal = Champion('이즈리얼', 700,90)
leesin = Champion('리신', 800,95)
yasuo = Champion('야스오', 750,92)
        
erzeal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()


#클래스 속성, 메스트

class class_n:
    def say(self):
        print('나는 몬스트다')

boblin =class_n()
boblin.say()

#자료형도 클래스다 

a = 10
b = '문자형객체'
c = True

print(b.__dir__())

print(type(a))
print(type(b))
print(type(c))

print(type(class_n()))
print(type(boblin.say()))