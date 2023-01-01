#t상속
#클래스들에 중복된 코드를 제거하고 유지보를 ㄹ 편하기 위해서 상ㅇ


class Monster:
    
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -=1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")
        
        
class wolf(Monster):
    pass

class shark(Monster):
    def move(self):#매서드 오버라이딩 (재정의)
        print(f"[{self.name}] 헤엄치기")
        
        
class Dragon(Monster):
    def move(self):#매서드 오버라이딩 (재정의)
        print(f"[{self.name}] 날기")
        
        
wolf = wolf('울프',1500, 200)
wolf.move()
print(wolf.max_num)

shark = shark('샤크', 3000, 400) 
shark.move()
print(Dragon.max_num)

Dragon = Dragon('드래곤', 8000, 800)
Dragon.move()
print(Dragon.max_num)