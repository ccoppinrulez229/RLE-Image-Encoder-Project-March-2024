r1=float(input("What is the value of R1? "))
r2=float(input("What is the value of R2? "))
r3=float(input("What is the value of R3? "))
#these are the input options for the r1-r3

resistance=1/((1/r1)+(1/r2)+(1/r3))
#this is the calculation for the resistance variable

resistance=round(resistance,2)
#this is rounding the previously calculated variable to 2 decimal places

print("The equivalent resistance is",resistance,"ohms")
#the final printed result