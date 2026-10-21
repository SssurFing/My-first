import random
class Cat:
    def __init__(self,name,fridge):
        self.name = name
        self.__age  = 0
        self.__hungery = 0
        self.__fatigued = 0
        self.fridge= fridge

    def life(self):
        if self.__hungery >= 100 or self.__fatigued >= 100:
            return False
        else:
            return True

    def hungry_level(self,hunger):
        self.__hungery+=hunger
        if self.__hungery >= 100:
            # print("die")
            pass
        elif self.__hungery<0 :
            self.__hungery = 0

    def fatigued_level(self,fatigue):
        self.__fatigued += fatigue
        if self.__fatigued >= 100:
            # print("die")
            pass
        elif self.__fatigued < 0:
            self.__fatigued = 0

    def eat(self,num):

        self.hungry_level(-num*30)
        self.fatigued_level(-num*40)
        self.fridge.reduce_fish(num)
        print(f'吃{num}条鱼，理论减{num * 30}饥饿度、{num * 40}疲劳度，冰箱剩余{self.fridge.get_fish()}条鱼')

    def rest(self):
        print(f'休息减{40}疲劳度')
        self.fatigued_level(-40)


    def fishing(self):
        print(f'钓鱼加20疲劳度 ',end='')
        self.fatigued_level(20)
        num = random.randint(0,3)
        print(f'钓到了{num}条鱼')
        self.fridge.add_fish(num)
        self.fridge.show_fish()

    def age_up(self):
        self.fatigued_level(10)
        self.hungry_level(10)
        self.__age+=1

    def show(self):
        print(f'当前{self.__age}岁的{self.name}饥饿度为{self.__hungery},疲劳度为{self.__fatigued}')

class Fridge:
    def __init__(self):
        self.fish_num=0

    def  get_fish(self):
        return self.fish_num

    def add_fish(self,num):
        self.fish_num+=num

    def reduce_fish(self,num):
        # if num <self.get_fish():
            self.fish_num-=num
        # else :
            # print("冰箱里的鱼不够了！")

    def show_fish(self):
        print(f'当前冰箱里有{self.get_fish()}条鱼')



def game_cat(cat):
    while 1:
        cat.age_up()
        cat.show()
        if cat.life() :
            pass
        else:
            print(f'你的{cat.name}死了！')
            break

        while 1 :
            ky = input("请输入（1-吃饭/2-钓鱼/3-休息）：")
            if  ky =='1':
                cat.fridge.show_fish()
                if cat.fridge.get_fish() == 0:
                    print("你有鱼么？你就吃？")
                    continue

                while 1:
                    try:
                        num = int(input("请输入吃鱼数："))
                        if num >cat.fridge.get_fish():
                            print("冰箱里的鱼不够了！")
                        elif num<0:
                            print("?")
                        else:
                            cat.eat(num)
                            break
                    except ValueError:
                        print("说猫话！")

            elif ky == '2':
                cat.fishing()

            elif ky == '3':
                cat.rest()
            else :
                print("说猫话！")
                continue
            break

        if cat.life() :
            pass
        else:
            print(f'你的{cat.name}死了！')
            break


if __name__ == '__main__':
    nm = input("你的猫叫啥？：")
    fridge1 = Fridge()
    Tom = Cat(nm,fridge1)
    game_cat(Tom)
    nm = input("你的猫叫啥？：")
    fridge1 = Fridge()
    Tom = Cat(nm, fridge1)
    game_cat(Tom)

    # while 1:
    #     cat.age_up()
    #     cat.show()
    #     if cat.life() :
    #         pass
    #     else:
    #         print("你猫死了！")
    #         break
    #
    #     while 1 :
    #         ky = input("请输入（1-吃饭/2-钓鱼/3-休息）：")
    #         if  ky =='1':
    #             cat.fridge.show_fish()
    #             if cat.fridge.get_fish() == 0:
    #                 print("你有鱼么？你就吃？")
    #                 continue
    #
    #             while 1:
    #                 try:
    #                     num = int(input("请输入吃鱼数："))
    #                     if num >cat.fridge.get_fish():
    #                         print("冰箱里的鱼不够了！")
    #                     elif num<0:
    #                         print("?")
    #                     else:
    #                         cat.eat(num)
    #                         break
    #                 except ValueError:
    #                     print("说猫话！")
    #
    #         elif ky == '2':
    #             cat.fishing()
    #
    #         elif ky == '3':
    #             cat.rest()
    #         else :
    #             print("说猫话！")
    #             continue
    #         break
    #
    #     if cat.life() :
    #         pass
    #     else:
    #         print("你猫死了！")
    #         break
