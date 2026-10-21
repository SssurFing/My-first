# a = range(int(input("输入n：")),int(input("输入m：")))
#
# b= list(a)
# b.append([1,2])
# print(b)
# b.insert(3,'jinqu')
# print(b)
# tol = 1
# for i in list(a):
#     tol*=i
#     print(i,tol)
# print(tol)


# import random
#
# a=list()
# for i in range(1,20):
#     a.append(random.randint(0,100))
# b=list()
# for i in a:
#     if i%2!=0:
#         b.append(i)
# print(b)


# a = ['熊大','熊二','熊三','熊四','熊五']
# for i in range(len(a)):
#     a.append(a[0])
#     del a[0]
#     print(a)


# import random
#
# a=[]
# for i in range(50):
#     a.append(random.randint(0,1000))
# print(a,'\n',len(a))
# a.sort()
# print(a)
# del a[0],a[-1]
# print(a)
# sum = 0
# for i in a:
#     sum+=i
# print(len(a))
# print(sum/len(a))


# a=[['北京','晴',2,35],['南京','晴',7,35],['郑州','晴',0,35],['新乡','晴',8,35]]
# dir=input("请输入城市：")
# for i in a:
#     if dir in i[0]:
#         print(i)
#         print(i[0],i[1],i[2],"-",i[3],'°')


# li_a=['啤酒','饮料','矿泉水','花生','瓜子','火腿肠']
# li_b=[]
# while(1):
#     k = input("请选择操作(1-查询商品清单，2-添加到购物车，3-从购物车删除，4-清空购物车,q-退出）：")
#
#     if k == "q":break
#
#     if k == "1":
#         print("货架商品清单如下",li_a)
#
#     if k == "2":
#         print("购物车：",li_b)
#         name = input("请输入要添加的商品名称:")
#
#         if name not in li_a:
#             print("商品名称不合法！")
#             continue
#
#         num = int(input("请输入要添加的商品个数:"))
#
#         if num <0:
#             print("商品个数不合法！")
#             continue
#
#         for i in li_b:
#             if name == i[0]:
#                 i[1]+=num
#                 break
#         else:
#             li_b.append([name,num])
#         print("加入购物车成功。当前购物车内商品名称和数量如下",li_b)
#
#     if k == "3":
#         print("购物车：", li_b)
#         name = input("请输入要删除的商品名称:")
#
#         if name not in li_a:
#             print("商品名称不合法！")
#             continue
#
#         num = int(input("请输入要删除的商品个数:"))
#
#
#         for i in li_b:
#             if name==i[0]:
#                 if num>i[1]:
#                     print("删除商品个数不合法！")
#                     break
#
#                 i[1]-=num
#                 if i[1] == 0:
#                     li_b.remove(i)
#                 break
#
#     if k == "4":
#         li_b.clear()
#         print("购物车：", li_b)


# address=('北京','郑州','南京','石家庄','太原','武汉','长沙')
# for i in range(len(address)):
#     for j in range(len(address)):
#         if i!=j:
#             print(address[i],"->",address[j])


# import random
# print("请输入5个数构成你的彩票！")
# cp_num = set()
# while len(cp_num)<5:
#     cp_num.add(random.randint(0,9))
#
# user_num = set()
# while len(user_num)<5:
#     a = int(input(f"您已输入{len(user_num)}个号码，请再输入一个："))
#     if a not in user_num:
#         user_num.add(a)
# print("你的彩票为：",user_num)
# print("中奖彩票为：",cp_num)
# print(user_num&cp_num)

# import pprint
# imag = {
#         '国家名' : '中华人民共和国',
#         '首都' : '北京',
#         '国土面积' : '960 万平方公里',
#         '建国时间' : '1949年10月',
#         '语言' : '汉语',
#         '文字' : '汉字'
# }
#
# # pprint.pprint(imag.values())
#
# for k in imag.keys():
#         print(k)
# for v in imag.values():
#         print(v)


# weather = {
#         '北京':{ '天气' : '晴' , ' 最高气温':27 , '最低气温':35},
#         '郑州':{ '天气' : '阵雨' , '最高气温':27 , '最低气温':32}
# }
# while 1:
#         city = input("city：")
#         for k ,v in weather[city].items():
#                 print(k,v)


# s = input("请输入一句话：")
# for i in s:
#         if i in '0123456789':
#                 print(i,end=' ')
# st=set()
# for i in s:
#     if i in '0123456789':
#             st.add(i)
# print(st)

# s = "板凳宽，扁担长。扁担没有板凳宽，板凳没有扁担长。扁担绑在板凳上，板凳不让扁担绑在板凳上，扁担偏要绑在板凳上"
# s1 = s.replace("板凳","bd").replace("扁担","板凳").replace("bd","扁担")
# print(s1)


# ming_xing={
#     '姓名':'悟空',
#     '性别':'男',
#     '年龄':1,
#     '特长': '七十二变',
#     '爱好': '偷吃蟠桃'
# }
# while 1 :
#     s = input("请输入 （1-查询信息，2-修改信息）：")
#     if s == "1":
#         s_k = input("请输入要查询的属性：")
#         print(ming_xing[s_k])
#     if s == "2":
#         s_k = input("请输入要修改的属性：")
#         s_v = input("请输入要修改的值：")
#         ming_xing[s_k] = s_v
