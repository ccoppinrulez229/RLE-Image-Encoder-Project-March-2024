m1=float(input("Enter m for Line 1: "))
b1=float(input("Enter b for Line 1: "))
m2=float(input("Enter m for Line 2: "))
b2=float(input("Enter b for Line 2: "))
#these are the inputs for the variables of m and b of lines 1 and 2

xint=(b2-b1)/(m1-m2)
yint=(m1*xint)+b1
#these are the calculations for the x and y coordinates of the intercept variables

xint=round(xint,2)
yint=round(yint,2)
#these are rounding the variables for the x and y coordinates of the intercept to 2 decimal places

print("The intersection point is (",xint,",",yint,")")
#the final printed result of the intersection point of 2 lines