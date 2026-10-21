import caiquan
import caishuzi

while 1:
    k = input("请选择游戏(1-石头剪刀布游戏、2-猜数字游戏)：")
    if  k =='1':
        caiquan.game()
    elif k == '2':
        caishuzi.game()
