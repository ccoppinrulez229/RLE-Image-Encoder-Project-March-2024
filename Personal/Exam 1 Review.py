#coding questions

#question 1
def identica_digits(x):
    while True:
        print(x,end=" ")
        if x%11==0:
            break
        x+=1

identica_digits(16)

print("")

#question 2
def print_triangle(base):
    for i in range (1,base+1):
        for j in range (1,i+1):
            print("*",end="")
        print("")
print_triangle(20)

#question 3
def is_prime(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                print("Not prime")
                return False
        print("Prime")
        return True
    else:
        print("Not prime")

is_prime(2)

#question 4
