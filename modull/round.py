def calculator():
    r= float(input("输入半径："))
    p = 3.14159
    mian =  p*r**2
    zhou = 2*p*r
    print(f'面积：{mian}。周长：{zhou}')
if __name__ == '__main__':
    print("圆形计算器")
    calculator()
