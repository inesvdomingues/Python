import random
 
symbols = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], ['0','1','2','3','4','5','6','7','8','9','!','#','$','%','&','?','*','+','-','.','_','<','>','º','«','»']]
p_size=input("Insert a password size: ")
p_quality=input("Insert a password strength [1-weak, 2-medium, 3-strong]: ")
 
passwd=''
for i in range(0,int(p_size)):
    #weak passwords only have lower letters, medium passwords have lower and upper letters and strong passwords have letters, numbers and symbols.
    n_array=random.randint(0,int(p_quality)-1)
    pos_array=random.randint(0,len(symbols[0])-1)
    passwd = passwd + str(symbols[n_array][pos_array])

print("Your new password: ", passwd)