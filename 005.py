import time as t
import datetime as dt
print(dt.datetime.now())
print(t.strftime("%Y:%M:%D %H:%M:%S"))
print(t.localtime())
'''
num = [2,3,5,7]
for count in range(2,1001):
    if count % 2 != 0 and count % 3 != 0 and count % 5 != 0 and count % 7 != 0:
        num.append(count)
print(num)
print(len(num))
'''
'''
ui = [] 
for i in range(2,1000):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
        if count == 2:
            if i == j:
                ui.append(i)
print(ui)
print(len(ui))
'''
x = lambda y: y ** y

print(x(10))
