# import random
#
# c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#
# yzm = random.choices(c,k=4)
# print(yzm)

# file = open(r"C:\Users\Lenovo\Desktop\输入法重启.txt")
# s = file.read()
# print(s)
# file.close()


# with open(r"C:\Users\Lenovo\Desktop\输入法重启.txt") as file :
#     s= file.read()
#     print(s)

# import datetime
# s = input("请输入yyyy-mm-dd格式的出生日期：")
# Bd = datetime.datetime.strptime(s,'%Y-%m-%d')
# Now = datetime.datetime.now()
# Long = Now -Bd
# print(Long.days)


# import datetime
# import logging
#
# def calculator_day():
#     logging.info('进入calculator_day函数。')
#     s = input("请输入目标日期（格式yyyy-mm-dd）：")
#     target = datetime.datetime.strptime(s,'%Y-%m-%d')
#     Now = datetime.datetime.now()
#     Long = target -Now
#     print(Long.days)
#
#
# if __name__ == '__main__':
#     logging.basicConfig(
#         filename='日志.log',
#         encoding='utf-8',
#         level=logging.DEBUG,
#     )


import requests

url = "http://uapis.cn/api/v1/misc/weather"
city = input("请输入城市：")
params = {
    'city' : city
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url,params=params,headers=headers )
resp.encoding= 'utf-8'
print(resp.text)