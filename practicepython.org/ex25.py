def main():
    print("Rules: \n  write + if your number is bigger;\n  write - if your number is smaller;\n  write = if the number is correct!")
    min = 0
    max = 100
    attempt_number = 0
    
    while True:
        #calculate the number:
        num = ((max-min)//2)+min
        feedback = input("Is the number {} ? ".format(num)) 
        attempt_number+=1
        
        #analyzes the user answer:
        if(feedback == "="):
            print("Nice, the computer won in {} attempt(s)!".format(attempt_number))  
            break
        elif(feedback == "+"):
            min=num
        else:
            max=num
    

if __name__ == "__main__":
    main()