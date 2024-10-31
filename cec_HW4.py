from console_gfx import ConsoleGfx #imports "ConsoleGfx" class from "console_gfx.py" file to be used throughout code

def to_hex_string(data): #translates data to a hexadecimal string
    string="" #string variable initialized as a blank string
    for i in data: #for loop that loops through the list and checks each number to convert to a specific hex string
        if i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8 or i==9:
            string+=str(i)
        if i==10:
            string+="a"
        if i==11:
            string+="b"
        if i==12:
            string+="c"
        if i==13:
            string+="d"
        if i==14:
            string+="e"
        if i==15:
            string+="f"
    return string #returns the final string

def count_runs(flat_data): #returns number of runs of data in an image data set
    run=0 #run variable initialized
    previousnum=flat_data[0] #sets previousnum variable to the first item in the flat_data list
    dupelist=[] #duplicate list that will be used to check whether or not a run exceeds 15 pixels
    for i in flat_data:
        if i==previousnum: #if the current iteration of i is the previous number, add i to the duplicate list.
            dupelist.append(i)
        else: #if the current iteration of i is not the previous number, check for pixel length of duplicates
            if len(dupelist)<15: #if the dupe list does not exceed 15 pixels...
                run+=1 #run variable increases by 1
                dupelist=[] #duplicate list gets reset
                previousnum=i #previousnum gets updated to the current iteration of i
                dupelist.append(i) #i is appended to dupelist
            else: #if the dupe list exceeds 15 pixels...
                while len(dupelist)>15: #keeps looping until dupelist does not exceed 15 pixels
                    dupelist=dupelist[15:] #remove the first 15 pixels in the duplicate list
                    run+=1 #run increases by 1, as every 15 pixels is considered one complete run.
                if len(dupelist) > 0: #after the while loop exhausts, if there are pixels remaining in the dupelist, increase run by 1.
                    run += 1
                previousnum=i #other variables get updated
                dupelist=[]
                dupelist.append(i)
    if len(dupelist) < 15: #accounts for the last number in the flat_data list
        run += 1
    else:
        while len(dupelist) > 15:
            dupelist = dupelist[15:]
            run += 1
        if len(dupelist)>0:
            run+=1
    return run

def encode_rle(flat_data):
    previousnum=flat_data[0] #previousnum variable initialized, set to the first number in the imported list
    rlelist=[] #rlelist variable initialized
    dupelist=[] #list to keep track and count how many duplicates of a number there are in a sequence, being reset whenever a new number is found
    for i in flat_data:
        if previousnum==i: #if the previous number is the same on the current iteration, add it to the dupe list
            dupelist.append(i)
        else: #if the previous number is not the same as the current iteration...
            while len(dupelist)>15: #while loop keeps going if there are more than 15 items in the duplicate list
                rlelist.extend([15, previousnum]) #a count of 15 with the previousnum variable are added to the list by default
                dupelist=dupelist[15:] #first 15 items are removed from the dupelist and its checked again. when loop exhausts, the remaining amount will be added to the list.
            rlelist.extend([len(dupelist),previousnum]) #extend the rle list with the count of instances of the number (with dupe list) followed by the number itself
            dupelist=[] #resets and appends the current iterarion to the dupe list
            dupelist.append(i)
            previousnum=i #previous number variable gets updated, starting the process over again
    while len(dupelist) > 15:  # while loop keeps going if there are more than 15 items in the duplicate list for the last number since previous loop does not account for the last number
        rlelist.extend([15, flat_data[-1]])
        dupelist = dupelist[15:]
    rlelist.extend([len(dupelist), flat_data[-1]]) #extends last number and its count to the rle list since loop does not account for that.

    return rlelist

def get_decoded_length(rle_data): #returns decompressed RLE data
    decodedlist=[] #decodedlist initialized, where all the numbers will go before counted
    timestoduplicate=0 #keeps track of the amount of times to duplicate a number based off position in the list
    num=0 #keeps track of number that will currently be duplicated to the list based on timestoduplicate variable
    while len(rle_data)>0: #while loop keeps going until there are no more items on the list. it will perfectly divide out by 2
        timestoduplicate=rle_data[0]
        num=rle_data[1]
        rle_data=rle_data[2:] #first two items are removed from the rle_data list. keeps going until there's none left
        for i in range (0,timestoduplicate): #for loop appends the specific number based on the amount of times it's duplicated
            decodedlist.append(num)
    return len(decodedlist) #length of the list is returned.

def decode_rle(rle_data):
    decodedlist = []  # decodedlist initialized, where all the numbers will go before counted
    timestoduplicate = 0  # keeps track of the amount of times to duplicate a number based off position in the list
    num = 0  # keeps track of number that will currently be duplicated to the list based on timestoduplicate variable
    while len(rle_data) > 0:  # while loop keeps going until there are no more items on the list. it will perfectly divide out by 2
        timestoduplicate = rle_data[0]
        num = rle_data[1]
        rle_data = rle_data[2:]  # first two items are removed from the rle_data list. keeps going until there's none left
        for i in range(0,timestoduplicate):  # for loop appends the specific number based on the amount of times it's duplicated
            decodedlist.append(num)
    return decodedlist  # length of the list is returned.

def string_to_data(data_string): #translates hexadecimal string to data
    data=[] #data list initialized
    for i in data_string: #for loop that loops through the list and checks each number to convert to a specific number
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            data.append(int(i))
        if i=="a" or i=="A":
            data.append(10)
        if i=="b" or i=="B":
            data.append(11)
        if i=="c" or i=="C":
            data.append(12)
        if i=="d" or i=="D":
            data.append(13)
        if i=="e" or i=="E":
            data.append(14)
        if i=="f" or i=="F":
            data.append(15)
    return data #returns the final list

def to_rle_string(rle_data): #Translates RLE data into a human-readable representation
    string="" #initializes string that will be returned
    while len(rle_data)>0: #loop keeps going as long as there are still numbers on the rle_data list
        string+=str(rle_data[0]) #adds the first number to the list, as it's just the count of the hexadecimal number
        if rle_data[1]==0 or rle_data[1]==1 or rle_data[1]==2 or rle_data[1]==3 or rle_data[1]==4 or rle_data[1]==5 or rle_data[1]==6 or rle_data[1]==7 or rle_data[1]==8 or rle_data[1]==9:
            string+=str(rle_data[1])
        if rle_data[1]==10:
            string+="a"
        if rle_data[1]==11:
            string+="b"
        if rle_data[1]==12:
            string+="c"
        if rle_data[1]==13:
            string+="d"
        if rle_data[1]==14:
            string+="e"
        if rle_data[1]==15:
            string+="f"
        #hexadecimal value is added to the string based on what's at index 0 in the rle_data list ^ ^
        rle_data=rle_data[2:] #removes first two items from the rle_data list after they've been added to the string
        if len(rle_data)!=0: #adds in delimiters ":" if the length of the list is still greater than 0 to separate the runs
            string+=":"
    return string #returns final string

def string_to_rle(rle_string): #translates a string in human-readable RLE format (w/ delimiters) into RLE byte data
    list=[] #rle list that will be returned is initialized
    currentstring="" #current string that will be converted to rle data is initialized
    hextoconvert="" #hextoformat string that will determine which hex number to convert to is initialized

    for i in rle_string: #for loop loops through the entire string that's put into the function
        if i!=":": #if the current iteration in the string is not a colon ":", append that specific item to the "currentstring" variable
            currentstring+=i
        else: #if the current iteration in the loop is a colon...
            hextoconvert=currentstring[-1] #hextoconvert variable is updated to the last character of the currentstring variable
            currentstring=currentstring[:-1] #currentstring variable is updated to include everything but the last character in the string
            list.append(int(currentstring)) #this remaining number will get added as an integer to the list

            if hextoconvert == "0" or hextoconvert == "1" or hextoconvert == "2" or hextoconvert == "3" or hextoconvert == "4" or hextoconvert == "5" or hextoconvert == "6" or hextoconvert == "7" or hextoconvert == "8" or hextoconvert == "9":
                list.append(int(hextoconvert)) #checks which number to convert to based on hexadecimal using hextoconvert variable
            if hextoconvert == "a" or hextoconvert == "A":
                list.append(10)
            if hextoconvert == "b" or hextoconvert == "B":
                list.append(11)
            if hextoconvert == "c" or hextoconvert == "C":
                list.append(12)
            if hextoconvert == "d" or hextoconvert == "D":
                list.append(13)
            if hextoconvert == "e" or hextoconvert == "E":
                list.append(14)
            if hextoconvert == "f" or hextoconvert == "F":
                list.append(15)
            currentstring="" #currentstring variable is reset to nothing.

    hextoconvert = currentstring[-1] #same code is placed after the for loop to take into account the remaining items left over in the currentstring variable.
    currentstring = currentstring[:-1]
    list.append(int(currentstring))

    if hextoconvert == "0" or hextoconvert == "1" or hextoconvert == "2" or hextoconvert == "3" or hextoconvert == "4" or hextoconvert == "5" or hextoconvert == "6" or hextoconvert == "7" or hextoconvert == "8" or hextoconvert == "9":
        list.append(int(hextoconvert))
    if hextoconvert == "a" or hextoconvert == "A":
        list.append(10)
    if hextoconvert == "b" or hextoconvert == "B":
        list.append(11)
    if hextoconvert == "c" or hextoconvert == "C":
        list.append(12)
    if hextoconvert == "d" or hextoconvert == "D":
        list.append(13)
    if hextoconvert == "e" or hextoconvert == "E":
        list.append(14)
    if hextoconvert == "f" or hextoconvert == "F":
        list.append(15)

    return list #list is returned.

def main(): #entire program nested in "main" function and will only be ran if it's in standalone mode
    list = [] #main list to decode lists and display images is initialized
    print("Welcome to the RLE image encoder!") #welcome message
    print("\nDisplaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)  # this function will be used to display different images, in this instance being the spectrum image. it builds images based off lists
    print("")
    while True:
        print("\nRLE Menu\n--------\n0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String") #menu is displayed
        print("4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        option=int(input("\nSelect a Menu Option: ")) #user input for menu option
        if option==1: #list gets cleared and updated to the decoded list based on the loaded file, which can then be displayed.
            filename=input("Enter name of file to load: ")
            list=ConsoleGfx.load_file(filename)
            print("")
        if option==2: #load test image
            list=ConsoleGfx.test_image #list gets updated to test_image's list in ConsoleGfx
            print("Test image data loaded.")
        if option==3: #Reads RLE data from the user in decimal notation with delimiters
            list=input("Enter an RLE string to be decoded: ")
            list=string_to_rle(list)
            list=decode_rle(list)
        if option==4: #reads RLE data from the user in hexadecimal notation without delimiters
            list=input("Enter the hex string holding RLE data: ")
            list=string_to_data(list)
            list=decode_rle(list)
        if option==5: #reads raw (flat) data from the user in hexadecimal notation
            list=input("Enter the hex string holding flat data: ")
            list=string_to_data(list)
        if option==6: #displays image from list
            print("Displaying image...")
            if len(list)>0: #will display image as long as a list of data is available
                ConsoleGfx.display_image(list)
                print("")
            else:
                print("(no data)")
        if option==7: #converts the current data into a human-readable RLE representation
            if len(list)>0: #will convert as long as a list of data is available
                list=encode_rle(list)
                print("RLE representation: ",to_rle_string(list))
                list=decode_rle(list)
            else:
                print("RLE representation: (no data)")
        if option==8: #converts the current data into RLE hexadecimal representation
            if len(list)>0: #will convert as long as a list of data is available
                list=encode_rle(list)
                print("RLE hex values: ", to_hex_string(list))
                list=decode_rle(list)
            else:
                print("RLE hex values: (no data)")
        if option==9: #displays the current raw (flat) data in hexadecimal representation
            if len(list)>0: #will convert as long as a list of data is available
                print("Flat hex values: ", to_hex_string(list))
            else:
                print("Flat hex values: (no data)")
        if option==0: #if option 0 is selected, stop the loop
            break
        if option>9 or option<0: #prints an error if the input is not between 0-9
            print("Error! Invalid input.")

if __name__=="__main__": #main() function that will be ran if the program is running as the main program
    main()