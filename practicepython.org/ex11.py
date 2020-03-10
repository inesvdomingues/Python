def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("The number is not prime.")
            return
    if num > 1:
        print("The number is prime!")
    else:
        print("The number is not prime.")


while True:
    num = input("Insert a number or write exit: ")
    if(num == "exit"):
        break
    else:
        is_prime(int(num))
