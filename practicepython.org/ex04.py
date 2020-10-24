num=int(input("insert a number: "))
li=[]
 
for i in range(1,num):
  if num % i ==0:
    #print("O número {} é divisor do {}".format(i,num))
    li.append(i)
print (li)