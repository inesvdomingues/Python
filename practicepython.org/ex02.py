num=input("number: ")
check=input("check: ")
 
if int(num)%2 == 0:
 if int(num)%4==0:
   print ("even number and multiple of 4")
 else:
   print ("even number")
else:
 print ("odd number")
 
if int(num)%int(check) == 0:
 print ("the check divides evenly into num")
else:
 print ("the check does not divides evenly into num")