import datetime
 
name=input("name: ")
age=input("age: ")
now = datetime.datetime.now()
print("You will turn 100 years old in: ",str((100-int(age))+now.year))