
import random
def cp():
    a = random.randint(1, 3)
    if a == 1:
        c_hand = "石头"
    elif a == 2:
        c_hand = "剪刀"
    else:
        c_hand = "布"
    return c_hand
def pd(c_hand,u_hand):
    if c_hand == u_hand:
        # print("平局")
        # peace+=1
        return 0
    elif (c_hand=="石头" and u_hand=="剪刀") \
        or((c_hand=="剪刀" and u_hand=="布") \
           or(c_hand=="布" and u_hand=="石头")):
        # print("电脑赢")
        # c_score+=1
        return -1
    else:
        # print("用户赢")
        # u_score+=1
        return 1
def caiquan_game():
    u_hand = input("请输入石头、剪刀或布：")
    c_hand = cp()
    result = pd(c_hand,u_hand)
    print("电脑出："+c_hand)
    if result == 1:
        print("用户赢")
    elif result == -1:
        print("电脑赢")
    else :
        print("平局")