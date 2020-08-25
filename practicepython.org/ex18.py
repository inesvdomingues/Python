import random
 
def cows_and_bulls(user_num, random_num):
    cows=0
    bulls=0
    
    for i in range(0,4):
        if str(user_num)[i]==str(random_num)[i]:
            cows+=1
        else:
            if (str(user_num)[i] in str(random_num)):
                bulls+=1
    
    print('You have %i cows and %i bulls.' %(cows, bulls))
    return
 
 
if __name__=="__main__":
 random_num= random.randint(1000,9999)
 print(random_num)
 
 while True:
   user_num=input("Insert a 4-digit number: ")
  
   if int(user_num) <1000 or int(user_num) > 9999:
     print("That is not a 4-digit number, try again!")
   else:
     if str(user_num)==str(random_num):
       print("You guess the number! ")
       break
     else:
       cows_and_bulls(user_num, random_num)

