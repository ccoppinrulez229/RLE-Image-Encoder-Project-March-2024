import math

print("Hello nigga. Today we're going to make sure yo bitch ass grasp the concepts from the hell that was Lab 2.")

num=int(input("\nFor starters, let's check if your number is prime or not nigga.\nType a number my nigga: "))

def is_prime(x):
    if x>1:
        for i in range(2,int(math.sqrt(x)+1)):
            if x%i==0:
                return False
        return True
    else:
        return False

print("\nIt is",is_prime(num),"that your number is prime my nigga")

print("\nNext, let's print out the prime factorization because of sum bullshit you were crying about all day")
num=int(input("\nType a new number my nigga (or don't; I don't give a fuck): "))

def print_prime_factor(x):
    div=2
    print(x,"=",end=" ")
    while x!=div and x!=1:
        while is_prime(div)==True and x%div==0 and x!=1:
            print(div,end=" ")
            x=x/div
            if x!=1:
                print("*",end=" ")
        div=div+1
    if x!=1:
        print(div,end="\n")

print_prime_factor(num)

print("\nGood job nigger. You can now successfully use functions and loops.")