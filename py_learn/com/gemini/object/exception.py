# def mul(a, b):
#     return a / b


def mul2(a, b):
    c = 0
    try:
       # c = a / b
        ls = []
        ls[10]
    except ZeroDivisionError:
        print("出错了。除数不能为o")
    except IndexError:
        print("索引异常。。。")
    except:
        print("未知异常。")
    return c


#print(mul(3, 4))
print(mul2(3, 0))
