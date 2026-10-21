import round
import squar

if __name__ == '__main__':
    while 1:
        key = input("输入正方形或圆形计算器：")
        if key=='正方形':
            squar.calculator()
        if key=='圆形':
            round.calculator()