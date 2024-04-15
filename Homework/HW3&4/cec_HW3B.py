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
        for i in range(0,
                       timestoduplicate):  # for loop appends the specific number based on the amount of times it's duplicated
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


from console_gfx import ConsoleGfx #imports "ConsoleGfx" class from "console_gfx.py" file to be used throughout code

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
        if option==2:
            list=ConsoleGfx.test_image
            print("Test image data loaded.")
        if option==3:
            testimage=0
        if option==4:
            testimage=0
        if option==5:
            testimage=0
        if option==6: #if "testimage" variable is enabled, display the test image. otherwise, display the list.
            print("Displaying image...")
            ConsoleGfx.display_image(list)
            print("")
        if option==7:
            testimage=0
        if option==8:
            testimage=0
        if option==9:
            testimage=0
        if option==0:
            break



if __name__=="__main__": #main() function that will be ran if the program is running as the main program
    main()