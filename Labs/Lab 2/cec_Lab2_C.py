#printed text displaying the available currencies
print("Available Currencies: A)USD B)CAD C)YEN")

#variables for the amount of money, the type of currency, and what currency to convert to
amount=float(input("Enter transaction amount: "))
currency=input("Transaction currency: ")
convert=input("Currency to convert to: ")

#conditional for whether or not currency conversion is needed and the parameters for what to convert the currency to
if not currency==convert:
    if currency=="A" and convert=="B":
        amount=round(amount*1.24,2)
        print("Converted value: ",amount,"CAD")
    elif currency=="A" and convert=="C":
        amount=round(amount*108.59,2)
        print("Converted value: ",amount,"YEN")
    if currency=="B" and convert=="A":
        amount=round(amount/1.24,2)
        print("Converted value: ",amount,"USD")
    elif currency=="B" and convert=="C":
        amount=round((amount/1.24)*108.59,2)
        print("Converted value: ",amount,"YEN")
    if currency=="C" and convert=="A":
        amount=round(amount/108.59,2)
        print("Converted value: ",amount,"USD")
    elif currency=="C" and convert=="B":
        amount=round((amount/108.59)*1.24,2)
        print("Converted value: ",amount,"CAD")
else:
    print("Conversion not needed...")