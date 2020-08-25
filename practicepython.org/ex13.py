sequence = [0,1]
 
def Fibonacci(num):
   if num<0:
       print("Incorrect number!")
   elif num<=len(sequence):
       return sequence[num-1]
   else:
       val = Fibonacci(num-1)+Fibonacci(num-2)
       sequence.append(val)
       return val
 
 
num=input("Insert a number: ")
Fibonacci(int(num))
print("Fibonacci sequence: ",sequence)