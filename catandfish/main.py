from Cels import Cat,Fridge
def game_cat(cat):
    while 1:
        cat.age_up()
        cat.show()
        if cat.life() :
            pass
        else:
            cat.die()
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
            cat.die()
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


# def hhh(cat):
#     while 1 :
#     if cat.life():
#         break
#     hungery = cat.get__hungery()
#     fatigued = cat.get__fatigued()
#     fish = cat.fridge.get_fish()
#     fish_num =0
#     if hungery > 70:
#         select = 3 #rest
#     elif fatigued  == 90 :
#         select = 1 #eating
#         fish_num = min(fish,3)
#     else:
#         select = 2 #fishing
#     main(select ,fish_num)