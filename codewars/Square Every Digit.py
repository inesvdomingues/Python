#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#Note: The function accepts an integer and returns an integer

def square_digits(num):
    results=[]
    num_str=str(num)
    
    for i in range (0,len(str(num))):      
        results.append(int(num_str[i])*int(num_str[i]))

    return int(''.join([str(elem) for elem in results]))

#def square_digits(num):
#    ret = ""
#    for x in str(num):
#        ret += str(int(x)**2)
#    return int(ret)

def main():
    print(square_digits(9119))
    
if __name__ == "__main__":
    main()