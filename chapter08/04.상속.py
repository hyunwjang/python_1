#t상속
#클래스들에 중복된 코드를 제거하고 유지보를 ㄹ 편하기 위해서 상ㅇ

#클래스 변서
#인스턴스들이 모두 공유하는 변수


import random

class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")
        
        
class wolf(Monster):
    pass


class shark(Monster):
    def move(self):#매서드 오버라이딩 (재정의)
        print(f"[{self.name}] 헤엄치기")
        
        
class Dragon(Monster):
    #생성자 오버라이딩
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ('불뿜기', '꼬리치기', '날개치기')
        
    def move(self):#매서드 오버라이딩 (재정의)
        print(f"[{self.name}] 날기")
        
    def skill(self):
        print(f"[{self.name}] 스킬사용 {self.skills[random.randint(0,2)]}")
        
        
        
wolf = wolf('울프',1500, 200)
wolf.move()

shark = shark('샤크', 3000, 400) 
shark.move()

Dragon = Dragon('드래곤', 8000, 800)
Dragon.move()
Dragon.skill()