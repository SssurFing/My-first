from box.game.caiquan import caiquan_game
from box.game.caishuzi import caishuzi_game
from box.program.round import round_calculator
from box.program.squar import squar_calculator



def menu():
    print("========== 功能主菜单 ==========")
    print("1. 圆形计算器")
    print("2. 正方形计算器")
    print("3. 石头剪刀布游戏")
    print("4. 猜数字游戏")
    print("0. 退出程序")
    print("================================")


if __name__ == '__main__':
    while 1:
        menu()
        re = input("请输入:")
        if re == '1':
            squar_calculator()
        elif re == '2':
            round_calculator()
        elif re == '3':
            caiquan_game()
        elif re == '4':
            caishuzi_game()
        elif re == '0':
            break
