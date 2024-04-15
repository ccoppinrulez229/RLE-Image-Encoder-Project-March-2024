import math

#fibonacci
def fibonacci(x):
    num1=0
    num2=1
    if x>1: #executes fibonacci loop if position (x) is greater than 1
        for i in range(0,x-2): #loops a certain number of times based on the position of the fibonacci number, updating num1 and num2 and adding them in the process
            sum=num1+num2
            num1=num2
            num2=sum
    else: #will automatically update sum to 0 if position is 1 because there are no other numbers available
        num2=0
    return num2 #returns num2 as the final position

#prime numbers
def is_prime(x):
    if x>1: #if the number is less than or equal to 1, it's automatically not a prime number
        for i in range(2,int(math.sqrt(x)+1)): #loop checking a certain number of times for possible divisible numbers
            if x%i==0:#if one of the numbers of i leaves a remainder of 0, the number is not a prime number
                return False
        return True #otherwise, the number is a prime number
    else:
        return False

#prime factorization
def print_prime_factors(x):
    print(x,"= ",end="")
    num=2 #variable for what's being divided into the number. will always be greater than 1 if it's prime
    while x!=num and x!=1:
        while is_prime(num) and x%num==0 and x!=1: #if num is a prime number, as long as there is a remainer of 0 when dividing num into x and x is >1, the loop will work.
            print(num,end=" ") #prints div if it's a prime number that leaves a remainder of 0 when divided in into x
            x=x/num #divides num into the x, updating x to a new value that can be used to find further prime numbers
            if x!=1: #as long as x does not equal 1, more multiplication can be done, thus another * is placed
                print("*",end=" ")
        num+=1 #will always add 1 to num even if previous while loop does not work, before looping back to the initial one. this will be used to determine all prime numbers from least to greatest
    if x!=1: #if above while loop exhausts and x does not equal 1, then the remaining num will be printed one last time.
        print(num,end="\n")
    return None

print_prime_factors(18)