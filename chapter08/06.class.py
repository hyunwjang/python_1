class item:
    def __init__(self, name, price, weigh, isdropable):
        self.name = name
        self.price = price
        self.weigh = weigh
        self.isdropable = isdropable
       
    def sale(self):
        print(f"[{self.name}] 판매가격은 [{self.price}]")  
        
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버렸습니다.")
        else:
            print(f"[{self.name}] 버릴수 없습니다.")
            
class WarebleTiem(item):
    def __init__(self, name, price, weigh, isdropable, effect):
        super().__init__(name, price, weigh, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 착용했습니다. [{self.effect}]")
            
class UsableTiem(item):
    def __init__(self, name, price, weigh, isdropable, effect):
        super().__init__(name, price, weigh, isdropable)
        self.effect =effect
    def use(self):
        print(f"[{self.name}] 사용했습니다. [{self.effect}]")
            
#인스턴스 생성

sword = WarebleTiem('이가닌자검', 3000, 3.5, True , "체력 500증가 마력 40000증가")
sword.wear()
sword.sale()
sword.discard()

potion = UsableTiem('신비한투명물약', 160000, 0.1, False, '투명효과 30초')
potion.use()
potion.sale()
potion.discard()
