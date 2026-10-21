def calculator():
    bian= float(input("输入正方形边长："))
    mian =  bian**2
    zhou = 4*bian
    print(f'面积：{mian}。周长：{zhou}')
if __name__ == '__main__':
    print("正方形计算器")
    calculator()
