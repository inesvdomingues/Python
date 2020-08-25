bdays = {"Marta":"20/07/1976", "Alberto":"02/03/1987", "Bianca": "17/02/1989"}
 
print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in bdays:
 print (i)
 
name=input("Who's birthday do you want to look up? ")
 
if name in bdays:
 print('{}\'s birthday is {}.'.format(name, bdays[name]))
else:
 print("Sadly, we don\' have {}\'s birthday.".format(name))
