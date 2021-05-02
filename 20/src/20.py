money = int(input())


class Alchohol:
    name = ''
    price = 0
    v = 0
    final_price = price
    final_v = v
    numb_of_bottle=0
    last_money=0

    def check_price(self):
        z = self.price
        while z < money:
            self.final_price += self.price
            self.final_v+=self.v
            self.numb_of_bottle+=1
            z += self.price
        self.last_money=money-self.final_price


    def display_info(self):
        print(self.name, self.numb_of_bottle)
        print(self.final_v)
        print(self.last_money)


k = int(input())

alco = []
for i in range(k):
    alco.append(Alchohol())

i = 0

while i < k:
    alco[i].name, alco[i].price, alco[i].v = input().split()
    alco[i].price=int(alco[i].price)
    alco[i].v = int(alco[i].v)
    alco[i].check_price()
    i += 1


alco[0].display_info()
