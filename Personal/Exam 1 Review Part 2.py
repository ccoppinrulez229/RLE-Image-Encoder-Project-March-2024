#good luck nigga

'''size=int(input("Enter base size: "))
for i in range(1,size+1):
    for j in range(1,i+1):
        print("*", end="")
    print("")


result="Your input: "
while True:
    num=int(input("Enter a number: "))
    if num!=999:
        result+=str(num) +","
    else:
        result+=str(num)
        break
print(result)


#factorial for loop
num=int(input("Enter a positive integer: "))
factorial=1
for i in range(num,0,-1):
    factorial*=i
print("The factorial of",num,"is:",factorial)


mass=float(input("The mass is: "))
velocity=float(input("The velocity is: "))
kine=(1/2)*(mass)*(velocity**2)
kine=round(kine,2)
print("The kinetic energy is:",kine)



h = float(input("Enter the value of h: "))
k = float(input("Enter the value of k: "))
r = float(input("Enter the radius r: "))
x1 = float(input("Enter the x coordinate of point P: "))
y1 = float(input("Enter the y coordinate of point P: "))
m = -(x1 - h) / (y1 - k)
b=(m*(-x1))+y1
m=round(m,2)
b=round(b,2)
if b>=0:
    print("The equation of the tangent line at P(",str(x1),",",str(y1),") is y=",m,"x +",b)
else:
    print("The equation of the tangent line at P(", str(x1), ",", str(y1), ") is y=", m,"x", b)

def increment(x):
    return x+1

a=5
a=increment(a)
print(a)


def celsius_to_farenheit(temp_in_celsius):
    return (9/5)*(temp_in_celsius)+32
def farenheit_to_celsius(temp_in_farenheit):
    return (5/9)*(temp_in_farenheit-32)

version=input("What format do you want to convert to? ")
if version=="farenheit":
    temperature=float(input("What is your temperature (C)?"))
    conversion=celsius_to_farenheit(temperature)
    conversion=round(conversion,2)
    print(temperature,"celsius is",conversion,"in farenheit")
if version=="celsius":
    temperature=float(input("What is your temperature (F)? "))
    conversion=farenheit_to_celsius(temperature)
    conversion=round(conversion,2)
    print(temperature,"farenheit is",conversion,"in celsius")'''

def is_divisible(a,b):
    if a%b==0 or b%a==0:
        return True
    else:
        return False

num1=int(input("First number:"))
num2=int(input("Second number:"))
if is_divisible(num1,num2):
    print("One is divisible by the other")
else:
    print("They are not divisible")


