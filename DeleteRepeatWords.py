def noRepeatWords(str):
    temp=str.split()
    temp.reverse()
    for i in temp:
            if temp.count(i)>1:
                    temp.remove(i)
    temp.reverse()
    return " ".join(temp)

if __name__=="__main__":
    str=input("please input some words:")
    print("Handle OK!",noRepeatWords(str))
