text=input("Insert a sentence: ")
words = text.split(" ")
#print("Inverted sentence: ",words[::-1])
 
new_text = ' '.join([str(w) for w in words[::-1]])
print(new_text)