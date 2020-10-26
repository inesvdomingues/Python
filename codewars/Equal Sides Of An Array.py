# You are going to be given an array of integers. 
# Your job is to take that array and find an index N where 
# the sum of the integers to the left of N is equal 
# to the sum of the integers to the right of N. 
# If there is no index that would make this happen, return -1.

def find_even_index(arr):    
    for i in range(0, len(arr),1):
        sum_r=sum(arr[:i])
        sum_l=sum(arr[(i+1):])
        if(sum_r == sum_l):
            return i
    return -1
        
    

def main():
    print (find_even_index([1,2,3,4,3,2,1])) #result: 3
    print (find_even_index([20,10,30,10,10,15,35])) #result: 3
    print (find_even_index([20,10,-80,10,10,15,35])) #result: 0
    print (find_even_index([10,-80,10,10,15,35,20])) #result: 6
    print (find_even_index(list(range(1,100))))  #result: -1
    print (find_even_index([0,0,0,0,0]))  #result: 0,"Should pick the first index if more cases are valid"
    print (find_even_index([-1,-2,-3,-4,-3,-2,-1]))  #result: 3
    print (find_even_index(list(range(-100,-1))))  #result: -1
    
if __name__ == "__main__":
    main()