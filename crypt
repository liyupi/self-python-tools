from itertools import cycle

def crypt(source,key):
    result=""
    a=cycle(key)
    for ch in source:
        result+=chr(ord(ch)^ord(next(a)))
    return result

if __name__=="__main__":
    source=input("输入想要加密/解密的字串:")
    key=input("输入密钥:")
    print("加密/解密成功!密码为:"+crypt(source,key))
