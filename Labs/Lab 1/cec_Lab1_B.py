import math

length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
#these are the input options for the variables of length and width

perimeter=(length*2)+(width*2)
area=length*width
diagonal=math.sqrt((length**2)+(width**2))
#these are the calculations for the variables of the rectangle's perimeter, area and diagonal length

perimeter=round(perimeter,2)
area=round(area,2)
diagonal=round(diagonal,2)
#these are rounding the variables for perimeter, area and diagonal 2 decimal places

print("Rectangle perimeter: ",perimeter)
print("Rectangle area: ",area)
print("Rectangle diagonal: ", diagonal)
#the final printed result