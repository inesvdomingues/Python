import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res = []

size_a= random.randint(0,50)
size_b= random.randint(0,50)
a= random.sample(range(1,101), size_a)
b= random.sample(range(1,101), size_b)

print ("List a: ", a)
print ("\nList b: ", b)

if (size_a>size_b):
 res = [num for num in a if num in b]
else:
 res = [num for num in b if num in a]
 
#set to avoid duplicates!
print ("\nList Overlap: ",set(res))
