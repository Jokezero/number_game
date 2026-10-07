import random
n = 0
a = random.randint(1,1000)
b = 0
while(True):
    b =input('请输入数字\n')
    if(int(b)==a):
        print("恭喜您猜中了，您一共猜测了"+str(n)+"次")
        break
    else:
        print("抱歉，没有猜中，请继续猜\n")
        if(int(b)>a):
            print("大了\n")
        if(int(b)<a):
            print("小了\n")
        n = n+1

