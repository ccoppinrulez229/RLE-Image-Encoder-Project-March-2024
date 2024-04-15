#variable input for water usage in gallons
gal = float(input("Enter your water usage in gallons: "))
cost = 0.0

#conditionals for whether or not the gallon is between a certain value, which calculates the final cost
if gal > 20000:
    cost = ((gal-20000)*(6.00/1000))+(14001*(3.75/1000))+ (5999*(2.35/1000))
elif gal>=6000 and gal<=20000:
    cost=((gal-5999)*(3.75/1000))+(5999*2.35/1000)
else:
    cost=(gal*(2.35/1000))

#this rounds the cost by 2 decimal places
cost=round(cost,2)

#final printed result
print("Money owed: $",cost)