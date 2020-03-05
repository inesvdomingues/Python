word=input("Insert a word: ")
 
control=0
for i in range(1, int(len(word)/2)+1):
 if(word[-i]!=word[i-1]):
   print("Not a palindrome!")
   control=1
   break
 
if(control==0):
 print("It's a palindrome!")
