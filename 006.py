from pyautogui import press   #导入需要的函数
from pyautogui import typewrite
from time import sleep
'''
消息轰炸机
1.首先先确定一下要发的内容以及次数
这里我用for循环
2.输出，模拟键盘操作，这里我使用了pyautogui
3.完成，输出 "轰炸完毕，感谢您的使用"
'''
test = input("请输入您要输出的内容：")  #使用input函数来进行东西的输入，并将它存在于test变量
count = input("请输入你要轰炸的次数：") #使用input来进行次数的输入，并将它存在于count变量，数据类型为字符串，为下一步的异样处理做准备
def hz(a,b):  #定义hz（轰炸）函数，使用了一个for以及上方导入的pyautogui的函数
    for x in range(a):
        typewrite(b)
        press("enter")
        sleep(0.25)
while True:    #主循环，判断是否为整数，否则就再输入
    try:
        count = int(count)
    except ValueError:
        print("请输入数字")
        count  = input("请输入您要轰炸的次数：")
    else:
        print("等待五秒，请在这五秒的时间内将光标置于对话的输入框内")
        sleep(5)
        hz(count,test)#上方定义的hz函数，意为轰炸
        break  #执行完毕，跳出循环
print("感谢您的使用，再见")  #感谢语
