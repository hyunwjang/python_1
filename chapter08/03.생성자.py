#생성자
#인스턴트를 만들때 호출되는 매섣드
#

class Moster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decreasc_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health   


#고블린 인스턴스 생성
goblin = Moster(800,120,300)
goblin.decreasc_health(100)
print(goblin.get_health())

#늑대 인스턴스 생성
wolf = Moster(1500, 200, 350)
wolf.decreasc_health(1000)
print(wolf.get_health())