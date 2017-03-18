import random

def redpacket(num,total):
    already=0
    each=[]
    for i in range(1,num):
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already=already+t
    each.append(total-already)
    myformat="第{0}个人拿了{1}分钱".format
    i=[i for i in range(1,num+1)]
    print(list(map(myformat,i,each)))

if __name__=="__main__":
    total=int(input("请输入红包金额(分)："))
    num=int(input("请输入抢红包人数："))
    redpacket(num,total)
