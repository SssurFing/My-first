# name = input("姓名：")
# age = input("年龄：")
# print(f'{name}的年龄是{age}岁。')




# def c(long , wide):
#     print(f"长方形的周长：{long*2+wide*2}")
# def s(long , wide):
#     print(f"长方形的面积：{long*wide}")
#
# long = int(input("请输入长方形的长："))
# wide = int(input("请输入长方形的宽："))
# c(long,wide)
# s(long,wide)


# def s():
#     long = float(input("请输入长方形的长："))
#     wide = float(input("请输入长方形的宽："))
#     return long*wide
# print(s())


# import random
# def s():
#     print("1-100以内猜数字，go！")
#     k= random.randint(0,100)
#     ci=0
#     while 1:
#         num = int(input("请输入："))
#         ci+=1
#         if num>k :
#             print("猜大了！再来")
#         elif num<k :
#             print("猜小了！再来")
#         elif num==k :
#             print("猜对了！")
#             return ci
#
# step={}
# while 1:
#     # k+=1
#     sp= int(s())
#     if sp in step:
#         step[sp]+=1
#     else:
#        step[sp]=1
#     for k ,v in step.items():
#         print(f'{k}次猜对了{v}局')


# zoo={
#     '猫' : '喵喵',
#     '狗' : '旺旺',
#     '鸡' : '咯咯哒',
#     '猪' : '哼哼'
# }
#
# def shut(k): =
#     if k in zoo:
#         print(f'{zoo[k]}')
# while 1:
#     shut(input("输入动物名："))

# def player(name,race='人',level='初入江湖',weapon='剑',skill='乱砍'):
#     print(f"{name}的种族是{race},他{level}，使用{weapon}，技能是{skill}")
# player(name='ss')
# player(name='aa',race='人',level='初入江湖',weapon='刀',skill='乱砍')

# tab = ['亿','千','百','十','','千','百','十','']
# tran = {
#     '1':'一',
#     '2':'二',
#     '3':'三',
#     '4':'四',
#     '5':'五',
#     '6':'六',
#     '7':'七',
#     '8':'八',
#     '9':'九',
#     '0':'零'
# }
# n = input("输入任意9位以内整数:")
# n_len = len(n)
# b= list(n)
#
# #数字转汉字
# for i in range(len(b)):
#     b[i] = tran[b[i]]
#
# f_zero=0
# f_mil=0
# mil_bo=0
# for i in range(n_len):
#     if f_mil==1 and n_len-i==4:
#         if b[-(n_len-i)]!='零':
#             print(b[-(n_len - i)], end="", sep="")
#         mil_bo=1
#         print("万",end="",sep="")
#
#
#     if f_zero and b[-(n_len-i)]=='零':
#         continue
#
#     if b[-(n_len-i)]=='零':
#         f_zero = 1
#         print(b[-(n_len-i)],end="",sep="")
#         continue
#     else:
#         f_zero = 0
#
#     print(b[-(n_len-i)],tab[-(n_len-i)],end="",sep="")
#     if 9>n_len-i>4:
#         f_mil=1
# print(b,n_len)


# tab = ['亿', '千万', '百万', '十万', '万', '千', '百', '十', '']
# # 数字映射汉字
# tran = {
#     '1': '一', '2': '二', '3': '三', '4': '四', '5': '五',
#     '6': '六', '7': '七', '8': '八', '9': '九', '0': '零'
# }
#
# while True:
#     n = input("输入任意9位以内整数:")
#     if n.isdigit() and len(n) <= 9:
#         break
#     print("输入不合法，请输入纯数字且位数不超过9位！")
#
# n_len = len(n)
# num_full = n.zfill(9)
# result = []
# zero_flag = False  # 标记是否上一位是零
#
# for idx in range(9):
#     num_char = num_full[idx]
#     han = tran[num_char]
#     unit = tab[idx]
#
#     if han == '零':
#         # 连续零只记录一次，不重复写入
#         if not zero_flag:
#             zero_flag = True
#             result.append('零')
#     else:
#         # 当前数字非零，先清除零标记
#         zero_flag = False
#         result.append(han)
#         # 个位不加单位
#         if unit != '':
#             result.append(unit)
#
# # 收尾处理：去除末尾多余的零
# if result and result[-1] == '零':
#     result.pop()
#
# # 特殊情况：数字全为0
# if not result:
#     print('零')
# else:
#     print(''.join(result))



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

# import random
# def cp():
#     a = random.randint(1, 3)
#     if a == 1:
#         c_hand = "石头"
#     elif a == 2:
#         c_hand = "剪刀"
#     else:
#         c_hand = "布"
#     return c_hand
# def pd(c_hand,u_hand):
#     if c_hand == u_hand:
#         # print("平局")
#         # peace+=1
#         return 0
#     elif (c_hand=="石头" and u_hand=="剪刀") \
#         or((c_hand=="剪刀" and u_hand=="布") \
#            or(c_hand=="布" and u_hand=="石头")):
#         # print("电脑赢")
#         # c_score+=1
#         return -1
#     else:
#         # print("用户赢")
#         # u_score+=1
#         return 1
#
# u_hand = input("请输入石头、剪刀或布：")
# c_hand = cp()
# result = pd(c_hand,u_hand)
# print("电脑出："+c_hand)
# if result == 1:
#     print("用户赢")
# elif result == -1:
#     print("电脑赢")
# else :
#     print("平局")


# 库存字典：商品名:[数量,单价]
stock = {"矿泉水":[50,2],"面包":[30,5]}

#1.增加商品
def add():
    name = input("商品名：")
    num = int(input("数量："))
    if name in stock:
        stock[name][0] += num
    else:
        price = float(input("单价："))
        stock[name] = [num, price]

#2.减少商品
def sub():
    name = input("商品名：")
    num = int(input("出库数量："))
    if name not in stock or num > stock[name][0]:
        print("操作失败")
    else:
        stock[name][0] -= num

#3.计算总价值
def total_price():
    total = 0
    for n,p in stock.values():
        total += n * p
    print("库存总价值：",total)

#菜单
while True:
    print(stock)
    print("\n1增加  2减少  3算总价  0退出")
    c = input("选择：")
    if c == "1":
        add()
    elif c == "2":
        sub()
    elif c == "3":
        total_price()
    elif c == "0":
        break
    else:
        print("输入错误")
