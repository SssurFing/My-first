# class Mouse:
#     love_food = '大米'
#     def __init__(self,name='none',love_food= "none"):
#         """初始化"""
#         self.name =name
#         self.love_food = love_food
#
#     def set_info(self,ip_name,ip_love_food):
#         # input_str=input("起个名字：")
#         self.name = ip_name
#         self.love_food = ip_love_food
#         self.eat()
#
#     def eat(self):
#         print(self.name+"吃了"+self.love_food)
#
#
#     @classmethod
#     def introduce(cls):
#         """类方法，不依赖实例变量"""
#         print(f'老鼠普遍爱吃{Mouse.love_food}')
#
# Mouse.introduce()
#
# JR = Mouse()
# JR.set_info('杰瑞','奶酪')
#
# JR.introduce()
# MLS = Mouse()
# MLS.set_info('MLS','大米')



# class Student:
#
#     def __init__(self,stu_id= "none",name= "none",course= "none"):
#         """初始化方法"""
#         self.name = name
#         self.stu_id = stu_id
#         self.course = course
#
#     def set_info(self,stu_id,name,course):
#         """设置信息"""
#         self.stu_id= stu_id
#         self.name = name
#         self.course = course
#
#     def show(self):
#         print(f'{self.stu_id},{self.name},{self.course}')
#
#
# a1 = Student()
# a2 = Student()
# a2.show()
# a1.set_info(123,'明明','数学')
# a1.show()


# class Role:
#     def __init__(self,name,hp,ap):
#         """
#         游戏角色
#         :param name:名字
#         :param hp: 生命力
#         :param ap: 攻击力
#         """
#         self.name = name
#         self.hp = hp
#         self.ap = ap
#
#     def attack(self,role):
#         role.hp -= self.ap
#         if role.hp >0:
#             print(f'{self.name}攻击了{role.name},{role.name}的生命力变为了{role.hp}')
#         else:
#             print(f'{self.name}攻击了{role.name},{role.name}死了')
#
#
# cat = Role('Tom',100,20)
# mouse = Role('Jr',90,25)
# cat.attack(mouse)
#
# cat.attack(mouse)
# cat.attack(mouse)
# cat.attack(mouse)
# cat.attack(mouse)


# class Player:
#     top_score = 0
#
#     def __init__(self,name):
#         self.name = name
#         self.score = 0
#     def add_score(self,score):
#         """增加积分"""
#         self.score +=score
#         print(f'{self.name}的积分增加了{score}，变为了{self.score}')
#         if self.score > self.top_score:
#             self.update_score(self.score)
#             print(f'{self.name}刷新了记录，新纪录是{self.score}')
#
#     @classmethod
#     def update_score(cls,score):
#         """更新记录"""
#         cls.top_score = score
#         cls.show_top()
#
#     @classmethod
#     def show_top(cls):
#         """展示记录"""
#         print(f'当前最高分纪录是：{cls.top_score}')
#
#
# class OutPlayer(Player):
#     def show_top(cls):
#         print(f'what  can i  say')
#         super().show_top()
#     def out(self):
#         self.show_top()
#         print(f'{self.name},out!')
#
# WestBrook = OutPlayer('WestBrook')
# WestBrook.out()
# ming = Player('ming')
# wang = Player('wang')
# while 1:
#     m= int(input("请输入ming的得分："))
#     w = int(input("请输入wang的得分："))
#     ming.add_score(m)
#     wang.add_score(w)
    # ming.show_top#
# ming.add_score(10)
# Player.show_top()




# class Goods :
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
# class SaleGoods(Goods):
#     def discount(self,price):
#         self.dis_price = price
#
# class Buyer:
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def buy(self):
#         pass
#
#
# class VipBuyer(Buyer):
#     def buy(self):
#         super().buy()



# class bank:
#     def __init__(self,id):
#         self.id = id
#         self.__yu_e = 0
#     def up_amount(self,amount):
#         self.__modify_amount(amount)
#     def down_amount(self,amount):
#         self.__modify_amount(-amount)
#     def __modify_amount(self,amount):
#         self.__yu_e+=amount
#         self.show_amount()
#     def get_amount(self):
#         return self.__yu_e
#     def show_amount(self):
#         print(f'当前余额{self.get_amount()}')
#
# tina = bank('1')
# while 1 :
#     ky = input("请选择1-存款/2-取款/3-查询余额：")
#     if ky == '1':
#         vl = int(input("存款数量："))
#         if vl > 0:
#             tina.up_amount(vl)
#
#     if ky == '2':
#         vl = int(input("取款数量："))
#         if vl > tina.get_amount():
#             print("余额不足!")
#         else:
#             tina.down_amount(vl)
#
#     if ky == '3':
#         tina.show_amount()


import random
class Cat:
    def __init__(self,name):
        self.name = name
        self.__age  = 0
        self.__hungery = 0
        self.__fatigued = 0

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
        fridge.reduce_fish(num)
        print(f'吃{num}条鱼，理论减{num * 30}饥饿度、{num * 40}疲劳度，冰箱剩余{fridge.get_fish()}条鱼')


    def rest(self):
        print(f'休息减{40}疲劳度')
        self.fatigued_level(-40)


    def fishing(self):
        print(f'钓鱼加20疲劳度 ',end='')
        self.fatigued_level(20)
        num = random.randint(0,3)
        print(f'钓到了{num}条鱼')
        fridge.add_fish(num)
        fridge.show_fish()

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

if __name__ == '__main__':
    fridge = Fridge()
    cat = Cat('Tom')
    while 1:
        cat.age_up()
        cat.show()
        if cat.life() :
            pass
        else:
            print("你猫死了！")
            break
        while 1 :
            ky = input("请输入（1-吃饭/2-钓鱼/3-休息）：")
            if  ky =='1':
                fridge.show_fish()
                if fridge.get_fish() == 0:
                    print("你有鱼么？你就吃？")
                    continue
                while 1:
                    try:
                        num = int(input("请输入吃鱼数："))
                        if num >fridge.get_fish():
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
            print("你猫死了！")
            break


# print("-----学生成绩计算器-----")
# score=[]
# while 1:
#     p = input("请输入一个成绩（输入q结束）：")
#     if p =='q':
#         break
#     else:
#         try:
#             point = int(p)
#             if 0 <= point <= 100 :
#                 score.append(point)
#             else :
#                 print("成绩必须在0~100之间！")
#         except ValueError:
#             print("输入非数字！")
#
# sum_score = sum(score)
# print(f'总分为{sum_score}')
#
# try:
#     avg_score = sum_score/len(score)
# except ZeroDivisionError:
#     print("除数为0！")
# else:
#     print(f'平均分为{avg_score}')
#     print("计算成功！继续努力！")
# finally:
#     print("程序执行完毕")

# import random
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0
#         self.__hungery = 0
#         self.__fatigued = 0
#
#     def life(self):
#         """判断猫是否活着，饥饿或疲劳>=100就死亡"""
#         if self.__hungery >= 100 or self.__fatigued >= 100:
#             return False
#         else:
#             return True
#
#     def hungry_level(self, hunger):
#         self.__hungery += hunger
#         if self.__hungery > 100:
#             self.__hungery = 100
#             print("die")
#         elif self.__hungery < 0:
#             self.__hungery = 0
#
#     def fatigued_level(self, fatigue):
#         # print(f'{self.__fatigued}<<<{fatigue}')
#         self.__fatigued += fatigue
#         if self.__fatigued > 100:
#             self.__fatigued = 100
#             print("die")
#         elif self.__fatigued < 0:
#             self.__fatigued = 0
#
#     def eat(self, num):
#         self.hungry_level(-num * 30)
#         self.fatigued_level(-num * 40)
#         fridge.reduce_fish(num)
#
#     def rest(self):
#         self.fatigued_level(-40)
#
#     def fishing(self):
#         self.fatigued_level(20)
#         num = random.randint(0, 3)
#         print(f'钓到了{num}条鱼')
#         fridge.add_fish(num)
#
#     def age_up(self):
#         """长大一岁，饥饿、疲劳各+10"""
#         self.fatigued_level(10)
#         self.hungry_level(10)
#         self.__age += 1
#
#     def show(self):
#         print(f'当前{self.__age}岁的{self.name}，饥饿度为{self.__hungery},疲劳度为{self.__fatigued}')
#
#
# class Fridge:
#     def __init__(self):
#         self.fish_num = 0
#
#     def get_fish(self):
#         return self.fish_num
#
#     def add_fish(self, num):
#         self.fish_num += num
#
#     def reduce_fish(self, num):
#         # 修复判断：鱼大于等于要消耗的数量，才扣减
#         if num <= self.get_fish():
#             self.fish_num -= num
#         else:
#             print("冰箱里的鱼不够了！")
#
#     def show_fish(self):
#         print(f'当前冰箱里有{self.get_fish()}条鱼')
#
#
# if __name__ == '__main__':
#     fridge = Fridge()
#     cat = Cat('Tom')
#     while True:
#         cat.age_up()
#
#         if not cat.life():
#             print("你的猫死了！游戏结束")
#             break
#
#         cat.show()
#         fridge.show_fish()
#
#         while True:
#             ky = input("\n请输入（1-吃饭/2-钓鱼/3-休息）：")
#             if ky == '1':
#                 num = int(input("请输入吃鱼数："))
#                 cat.eat(num)
#             elif ky == '2':
#                 cat.fishing()
#             elif ky == '3':
#                 cat.rest()
#             else:
#                 print("说猫话！请输入1、2、3")
#                 continue
#             # 操作完成后，跳出内层循环，进入下一岁
#             break


# import random
#
# def game():
#     num = random.randint(1,100)
#     step=0
#
#     win = False
#     while not win:
#         try:
#             x = int(input("请输入一个整数："))
#         except ValueError:
#             # 输入不是数字，警告，步数+1
#             print("警告！你输入的不是数字！")
#             step += 1
#             continue  # 直接回到循环开头，重新输入
#
#         step+=1
#         if x == num:
#             print("猜对了")
#             win = True
#         elif x>num :
#             print("猜大了")
#         else :
#             print("猜小了")
#     print(f'一共用了{step}步')
#     if step <= 1:
#         print("真厉害，你简直是个奇迹！")
#     elif step <=3:
#         print("真厉害，这么快就猜对了！")
#     elif step <=5:
#         print("恭喜你，猜对了！")
#     else:
#         print("你终于猜出来了！")
#
# game()