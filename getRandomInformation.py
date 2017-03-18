 import string
import codecs
import random

def getInformation(num):
    character=string.ascii_letters+string.digits+'_'
    StringBase='\u7684\u4e00\u4e86\u4e0d\u5728\u4eba\u662f\u6211\u2313\u3212\u6544'
    StringBase="".join(StringBase.split())
    result=""
    if num==0:
        for i in range(random.randint(2,4)):
            result+=random.choice(StringBase)
        return result
    elif num==1:
        result=random.choice("男女")
        return result
    elif num==2:
        result=str(random.randint(1,100))
        return result
    elif num==3:
        for i in range(random.randint(7,9)):
            result+=random.choice(string.digits)
        return result
    elif num==4:
        result="".join([random.choice(string.digits) for i in range(random.randint(5,10))])
        return result
    elif num==5:
        endurl=[".com",".org",".cn",".net"]
        username="".join([random.choice(character) for i in range(6,12)])
        domain="".join((random.choice(character) for i in range(3,6)))
        result=username+"@"+domain+random.choice(endurl)
        return result
    
if __name__=="__main__":
    print("随机生成的用户信息如下:")
    print("姓名:"+getInformation(0))
    print("性别:"+getInformation(1))
    print("年龄:"+getInformation(2))
    print("电话:"+getInformation(3))
    print("QQ号:"+getInformation(4))
    print("邮箱:"+getInformation(5))
