li = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = []
 
num=input("insert a number: ")
for i in li:
  if(i<int(num)):
    #print(i)
    res.append(i)
print (res)
 
#one line extra:
print (list(filter(lambda x: x < int(num), li)))