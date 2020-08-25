num1=input("numero 1: ")
num2=input("numero 2: ")
num3=input("numero 3: ")

if int(num1)>int(num2):
  print("")
  if int(num1)>int(num3):
    print("num1")
  else:
    print("num3")
elif int(num2)>int(num3):
  print("num2")
else:
  print("num3")
