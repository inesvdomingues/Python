def li(a_list):
    return [a_list[0], a_list[len(a_list)-1]]
 
 
while True:
    num=[]
    num=input("Insert a list: ")
    if(num=="exit"):
        break
    else:
        print("List ends: ", li(num))
