#these are the variable inputs for each side of the triangle
a=float(input("Enter side 1: "))
b=float(input("Enter side 2: "))
c=float(input("Enter side 3: "))

#this is the condition for determining whether the triangle has a right angle using the pythagorean theorem
if (c**2 == a**2+b**2) or (a**2 == c**2+b**2) or (b**2 == a**2+c**2):
    print("This triangle has a right angle!")
else:
    print("This triangle doesn't have a right angle...")