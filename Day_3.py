#分别询问猪八戒和沙和尚的武力值 法力值 智力值然后进行各项能力比较和总能力值比较
# wuli1 = int(input("请输入猪八戒的武力值："))
# wuli2 = int(input("请输入沙和尚的武力值："))
# fali1 = int(input("请输入猪八戒的法力值："))
# fali2 = int(input("请输入沙和尚的法力值："))
# zhi1 = int(input("请输入猪八戒的智力值："))
# zhi2 = int(input("请输入沙和尚的智力值："))
# print("猪八戒的武力值比沙和尚高吗？",wuli1>wuli2)
# print("猪八戒的法力值比沙和尚高吗？",fali1>fali2)
# print("猪八戒的智力值比沙和尚高吗？",zhi1>zhi2)
# print("猪八戒的总能力比沙和尚高吗？",(wuli1+fali1+zhi1)>(wuli2+fali2+zhi2))


# yw = int (input("语文成绩："))
# sx = int (input("数学成绩："))
# fs = int (input("法术成绩："))
# print("孙悟空每门课都及格了吗？",yw>=60 and sx>=60 and fs>=60)
# print("孙悟空该科了吗？",yw<60 or sx<60 or fs<60)
# print("孙悟空最好的课是法术吗？",fs>yw and fs>sx)


# u_id = input("请输入用户名：")
# u_pwd = input("请输入密码：")
# if u_id == "SunWukong" and u_pwd == "QiTianDaSheng":
#     print("登录成功")
# else:
#     print("用户名或密码错误")


# born = int(input("请输入出生年份："))
# year = 2026
# if(year-born)>=18:
#     print("已成年")
# else:
#     print("未成年,再过"+str(18-(year-born))+"年成年")


# u_id = input("请输入用户名：")
# u_pwd = input("请输入密码：")
# if u_id == "SunWuKong" and u_pwd == "QiTianDaSheng":
#     print("登录成功")
# else:
#     if u_id != "SunWuKong":
#         print("用户名不存在")
#     elif u_pwd != "QiTianDaSheng":
#         print("密码错误")
# print("end")


# u_id = input("请输入用户名：")
# u_pwd = input("请输入密码：")
# id="SunWuKong"
# pwd="QiTianDaSheng"
# if u_id == id:
#     if u_pwd == pwd:
#         print("登录成功")
#     else:
#         print("密码错误")
# else:
#     print("用户名不存在")
# print("end")


# import random
# u_hand = input("请输入石头、剪刀或布：")
#
# a = random.randint(1,3)
# if a == 1:
#     c_hand ="石头"
# elif a == 2:
#     c_hand = "剪刀"
# else:
#     c_hand = "布"
# print(c_hand)
# if c_hand == u_hand:
#     print("平局")
# elif (c_hand=="石头" and u_hand=="剪刀") \
#     or((c_hand=="剪刀" and u_hand=="布") \
#        or(c_hand=="布" and u_hand=="石头")):
#     print("电脑赢")
# else:
#     print("用户赢")


# a= int(input("第一个数："))
# b= int(input("第二个数："))
# c= int(input("第三个数："))
# # if a>=b and a>=c:
# #     print("最大值："+str(a))
# #     if b>=c:
# #         print("最小值："+str(c))
# #     else:
# #         print("最小值："+str(b))
# # elif b>=a and b>=c:
# #     print("最大值："+str(b))
# #     if a>=c:
# #         print("最小值："+str(c))
# #     else:
# #         print("最小值："+str(a))
# # elif c>=b and c>=a:
# #     print("最大值："+str(c))
# #     if a>=b:
# #         print("最小值："+str(b))
# #     else:
# #         print("最小值："+str(a))
# if a>=b and a>=c:
#     print("最大值："+str(a))
# elif b>=a and b>=c:
#     print("最大值："+str(b))
# elif c>=b and c>=a:
#     print("最大值："+str(c))
# if b>=a and c>=a:
#     print("最小值："+str(a))
# elif a>=b and c>=b:
#     print("最小值："+str(b))
# elif a>=c and b>=c:
#     print("最小值："+str(c))


# yj= int(input("请输入原价："))
# res= yj
# age = int(input("请输入购票人年龄："))
# wk = input("是否周末：")
# fs = input("是否节假日：")
# if age<6:
#     res=0
# else:
#     if age<18:
#         res*=0.7
#     elif age>65:
#         res*=0.8
#     if wk=="是":
#         res+=yj*0.1
#     if fs=="是":
#         res+=yj*0.2
#
# print(res)


# k=0
# for i in range(2000,2501):
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print(i,end=" ")
#         k+=1
#         if k%10==0:
#             print("")
# print("\n"+str(k))


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",j*i,end="\t",sep="")
#     print("")


# import random
#
# u_score=0
# c_score=0
# peace=0
# for i in range(3):
#     u_hand = input("请输入石头、剪刀或布：")
#
#     a = random.randint(1,3)
#     if a == 1:
#         c_hand ="石头"
#     elif a == 2:
#         c_hand = "剪刀"
#     else:
#         c_hand = "布"
#     print("电脑出："+c_hand)
#     if c_hand == u_hand:
#         # print("平局")
#         peace+=1
#     elif (c_hand=="石头" and u_hand=="剪刀") \
#         or((c_hand=="剪刀" and u_hand=="布") \
#            or(c_hand=="布" and u_hand=="石头")):
#         # print("电脑赢")
#         c_score+=1
#     else:
#         # print("用户赢")
#         u_score+=1
#
# print("玩家赢",u_score,"次")
# print("电脑赢",c_score,"次")
# print("平局",peace,"次")


# n= int(input("请输入比赛局数："))
# p1= input("请输入甲方名称：")
# p2= input("请输入乙方名称：")
# p1_score = 0
# p2_score = 0
# for i in range(n):
#     k=int(input("请输入得分方（1/2）："))
#     if k==1:
#         p1_score+=1
#     elif k==2 :
#         p2_score+=1
#     print("当前最新比分：",p1_score,":",p2_score)
# print("end")


# tol = int(input("请输入鸡兔同笼中脚的总数："))
# res=0
# for rabit in range(0,tol//4+1):
#     chicken = (tol-rabit*4)//2
#     if rabit*4+chicken*2==tol:
#         res+=1
#         print("鸡：",chicken," 兔：",rabit)
# if res == 0 :
#     print("不可能")
# else :
#     print("共",res,"种可能")


import random

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


p1= input("请输入甲方名称：")
p2= input("请输入乙方名称：")
p1_score = 0
p2_score = 0
print("比赛开始，输入q结束比赛")
while True:
    k=input("请输入得分方（1-甲/2-乙/q-结束比赛 ）：")
    if k=="1":
        p1_score+=1
    elif k=="2" :
        p2_score+=1
    elif k=="q":
        break
    print("当前最新比分：",p1_score,":",p2_score)
print("比赛结束")
print("最终比分：",p1_score,":",p2_score)
print("end")