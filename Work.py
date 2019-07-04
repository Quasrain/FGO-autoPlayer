# encodeing = utf-8
import os
import time
import random
import config

def Click(x,y,Time):
    x = int(x * XSize + random.random())
    y = int(y * YSize + random.random())
    command = 'adb shell input tap '+str(y)+' '+str(x)
    os.system(command)
    print(command)
    time.sleep(Time)

def Swipe(x1,y1,x2,y2,Time):
    x1 = x1 * XSize + random.random()
    x2 = x2 * XSize + random.random()
    y1 = y1 * YSize + random.random()
    y2 = y2 * YSize + random.random()
    command = 'adb shell input swipe ' + str(y1) + ' ' + str(x1) + ' ' + str(y2) + ' ' + str(x2)
    os.system(command)
    print(command)
    time.sleep(Time)

def FindTask():
    # 从主菜单开始,选择“迦勒底之门”，由于奇怪的记忆机制，决定先拉到顶再往下拉
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.4)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Click(0.75,0.8,random.random()+0.4)
    # 往下滑动，找到“每日任务”，由于奇怪的记忆机制，决定先拉到顶再往下拉
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.4)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.4, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.8,0.8,0.2,0.8,random.random()+0.4)
    # 点击“每日任务”
    Click(0.7,0.8,random.random())


def Fight():
    # 进入每日任务后,直接找到最高级的狗粮本
    ## 由于练度问题，选第三个
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.4)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.3, 0.8, 0.9, 0.8, random.random() + 0.2)
    Swipe(0.4, 0.8, 0.9, 0.8, random.random() + 0.2)
    Click(0.8, 0.7, random.random() + 3)
    # 选择助战
    Click(0.4, 0.7, random.random() * 3)
    # 开始任务
    Click(0.9, 0.9, random.random() + 7)
    while True:
        # Attack
        Click(0.9,0.9,random.random()+0.2)
        number = [0,1,2,3,4]
        x = 0.7
        y = [0.1,0.3,0.5,0.7,0.9]
        random.shuffle(number)
        for i in range(3):
            Click(0.3,y[i+1],0)
        for i in range(3):
            Click(0.75,y[number[i]],0)
        time.sleep(5)
        for i in range(5):
            Swipe(random.random(),random.random(),random.random(),random.random(),0)
        time.sleep(5)

if __name__ == '__main__':
    XSize = int(config.XSize)
    YSize = int(config.YSize)
    # 找到对应的任务，默认为每日最高级的狗粮本
    FindTask()
    # 进入战斗
    Fight()