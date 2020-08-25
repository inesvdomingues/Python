def PROC(li, num):
    for i in range(len(li)):
        if (li[i] == int(num)):
            return True
    return False
 
if __name__=="__main__":
    li = [2, 4, 6, 8, 10]
    num=input("Número: ")
    print (PROC(li,num))
