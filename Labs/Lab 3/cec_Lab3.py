import math
#variables for displaying the menu, total sum of calculations, number of calculations and the current calculation
displaymenu=1
sumcalcs=0
numcalcs=0
current=0.0

print("Current Result: ",current)

#nested while condition to keep showing calculator after each calculation
while displaymenu==1:
    print('''
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average''')
    selection=int(input("\nEnter Menu Selection: ")) #checks for whether or not the selection is valid.
    if selection==7: #average, displaying based on whether or not the total number of calculations made is > 0
        if numcalcs>0:
            print("\nSum of calculations: ",sumcalcs)
            print("Number of calculations: ", numcalcs)
            average=sumcalcs/numcalcs
            average=round(average,2)
            print("Average of calculations: ",average)
            selection = int(input("\nEnter Menu Selection: "))
        else:
            print("Error: No calculations yet to average!")
            selection = int(input("\nEnter Menu Selection: "))
    if selection>0 and selection<7: #if it's a valid selection, user can input their operands
        operand1=float(input("Enter first operand: "))
        operand2=float(input("Enter second operand:"))
    else: #if it's not a valid selection, it will keep looping back until it's valid
        while selection<0 or selection>7:
            print("\nError: Invalid selection!")
            selection = int(input("\nEnter Menu Selection: "))
    if selection==0: #if selection is 0, loop ends
        print("\nThanks for using this calculator. Goodbye!")
        displaymenu=0
    if selection==1: #addition
        current = operand1 + operand2
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)
    if selection==2: #subtraction
        current = operand1 - operand2
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)
    if selection==3: #multiplication
        current = operand1 * operand2
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)
    if selection==4: #division
        current = operand1 / operand2
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)
    if selection==5: #exponentiation
        current = operand1**operand2
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)
    if selection==6: #logarithm
        current = math.log(operand2,operand1)
        current = round(current, 2)
        sumcalcs = sumcalcs+current
        numcalcs = numcalcs+1
        print("\nCurrent Result: ", current)