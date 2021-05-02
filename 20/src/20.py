class Alchohol:
    name = ''
    price = 1
    v = 1
    final_price=0
    final_v=0

    def check_price(self):





        print(self.name)

    def display_info(self):
        print(self.name)


money = int(input())
k = int(input())
alco = [Alchohol()]
i = 0

while i < k:
    alco[i].name, alco[i].price, alco[i].v = input().split()
    i += 1

alco[0].display_info()
