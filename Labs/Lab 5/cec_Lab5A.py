def hex_char_decode(digit): #decodes a single hexadecimal digit and returns its value
    if digit=="0":
        return 0
    if digit=="1":
        return 1
    if digit=="2":
        return 2
    if digit=="3":
        return 3
    if digit=="4":
        return 4
    if digit=="5":
        return 5
    if digit=="6":
        return 6
    if digit=="7":
        return 7
    if digit=="8":
        return 8
    if digit=="9":
        return 9
    if digit=="A" or digit=="a":
        return 10
    if digit=="B" or digit=="b":
        return 11
    if digit=="C" or digit=="c":
        return 12
    if digit=="D" or digit=="d":
        return 13
    if digit=="E" or digit=="e":
        return 14
    if digit=="F" or digit=="f":
        return 15

def hex_string_decode(hex): #decodes an entire hexadecimal string and returns its value
    result=0 #result and exponent initialized as 0
    exponent=0
    if hex[0:2] == "0x":  # if the input string starts with "0x", remove those two characters
        hex = hex[2:]
    reversedstring = hex[::-1]  # reverses the string that's input
    for i in reversedstring: #for loop that goes through and decodes each number in the string
        decodednumber = hex_char_decode(i)  # decodes each hexadecimal digit by going through the "hex_char_decode" function and returns the value to the "decodednumber" variable
        result+=decodednumber*(16**exponent) #converts specific hexadecimal in the loop to a decimal number, adding them to the total result.
        exponent += 1 #exponent increases by 1 each time on subsequent loops
    return result

def binary_string_decode(binary): #decodes a binary string and returns its value
    result=0 #result and exponent initialized as 0
    exponent=0
    if binary[0:2] == "0b":  # if the input string starts with "0b", remove those two characters
        binary = binary[2:]
    reversedstring = binary[::-1]  # reverses the string that's input
    for i in reversedstring: #for loop that goes through converts each binary number to a decimal, adding up the total
        if i=="0": #if i is "0" in the loop, 0 is added to the total
            result+=0*(2**exponent)
            exponent+=1
        else: #otherwise, i will be "1" and have 1 times 2 raised to whatever exponent added to the total
            result+=1*(2**exponent)
            exponent+=1
    return result

def binary_to_hex(binary): #Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
    splitstring=""
    finalstring= ""
    result=0
    while len(binary)!=0: #loop keeps going until there are no more characters left.
        splitstring=binary[0:4] #splitstring variable gets updated to first 4 digits of the binary string called into the function
        binary=binary[4:] #binary string gets updated, removing first 4 characters. loop persists until there are no more characters left
        reversedstring = splitstring[::-1]  # reverses the string of what's split from the string that was input
        exponent=0 #exponent gets reset whenever a new group will be decoded
        for i in reversedstring:
            if i=="0": #if i is "0" in the loop, 0 is added to the total
                result+=0
                exponent+=1
            if i=="1": #otherwise, i will be "1" and have 1 times 2 raised to whatever exponent added to the total
                result+=1*(2**exponent)
                exponent+=1
        if result<=9: #once for loop exhausts through the characters of the split binary, it checks to see what to add to the final string based on what the result was.
            finalstring+= str(result)
        if result==10:
            finalstring+="A"
        if result==11:
            finalstring+="B"
        if result==12:
            finalstring+="C"
        if result==13:
            finalstring+="D"
        if result==14:
            finalstring+="E"
        if result==15:
            finalstring+="F"
        result=0 #result gets reset back to 0 to look for next group
    return finalstring #once while loop exhausts, the final string is returned and printed.

def main():
    while True: #shows main decoding menu, prompting the user to enter an option. will keep looping back until loop is broken.
        result=""
        convertedstring=""
        print(("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit"))
        option=input("\nPlease enter an option: ")

        if option=="1":
            string = input("Please enter the numeric string to convert: ")
            decodedhex=hex_string_decode(string) #reversed string is placed into the upper function, to decode its entirety and return its value
            print("Result: ",decodedhex,"\n",sep="")

        if option=="2":
            string = input("Please enter the numeric string to convert: ")
            decodedbinary=binary_string_decode(string)
            print("Result: ",decodedbinary,"\n",sep="")

        if option=="3":
            string = input("Please enter the numeric string to convert: ")
            if len(string)<8:
                while len(string)!=8: #while the length of the string does not equal 8, keep adding "0" to the beginning of the string.
                    string="0"+string
            bintohex=binary_to_hex(string)
            print("Result: ",bintohex,"\n",sep="")

        if option=="4":
            break

if __name__ == "__main__": #main function
    main()