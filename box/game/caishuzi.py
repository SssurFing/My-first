import random
def caishuzi_game():
    num = random.randint(1,100)
    step=0

    win = False
    while not win:
        x = int(input("请输入一个整数："))
        step+=1
        if x == num:
            print("猜对了")
            win = True
        elif x>num :
            print("猜大了")
        else :
            print("猜小了")
    if step <= 1:
        print("真厉害，你简直是个奇迹！")
    elif step <=3:
        print("真厉害，这么快就猜对了！")
    elif step <=5:
        print("恭喜你，猜对了！")
    else:
        print("你终于猜出来了！")