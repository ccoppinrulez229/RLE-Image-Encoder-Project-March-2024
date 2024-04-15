import sys #sys is imported, allowing for use of the terminal
from heifer_generator import HeiferGenerator as HG #HeiferGenerator is imported and binded to a variable HG allowing for the use of the get_cows() function

def list_cows(cows): #displays the available cows from a python list of available objects
    iteration=0 #iteration variable is initialized
    string="" #string is initialized
    for i in cows: #for loop goes through each cow and adds their name to the string variable
        string+=str(cows[iteration].get_name())+" " #adds the name of the current iteration of the cow list into the string, with the two available cows being "heifer" and "kitteh"
        iteration+=1 #increases iteration by 1 each time
    print("Cows available: ",string,"\n",sep="") #prints final string result
    pass

def find_cow(name,cows): #given a name and python list of cow objects, return the Cow object with the specified name
    iteration=0 #iteration variable is initialized
    for i in cows: #for loop will go through each cow to see if the name matches
        if str(cows[iteration].get_name())==name: #if the name of the cow matches the name that's put in the function, return the cow image at that iteration
            return cows[iteration].get_image()
        elif str(cows[iteration].get_name())!=name: #if it does not, increase iteration by 1 and check again
            iteration+=1

    print("Could not find",name,"cow!\n")  #if above loop exhausts and the name does not match either cow, print error message and return None
    return None
    pass

def main():
    args = sys.argv #creates an args variable with sys.argv, allowing user input in terminal to be converted into a list
    cows = HG.get_cows() #generates the available cow objects into a list using the heifer generator class. will be used to determine data
    if sys.argv[1]=="-l": #if -l is present in the sys list at the specified position, display the list of all available cows
        list_cows(cows)

    elif sys.argv[1]=="-n": #if -l is present in the sys list at the specified location, display the cow and message
        cow = find_cow(sys.argv[2],cows)  # cow variable is initialized with find_cow function, using the name at position 2 in sys list and cows list as reference
        message="" #message variable is initialized
        if cow!=None: #if a valid cow name is chosen, print the message and display the cow
            for i in sys.argv[3:]: #for loop adds every item to the sys list from position 3 onwards, creating the message
                message+=i+" "
            print("\n",message,sep="") #message is printed before the cow is displayed
            print(cow) #after the specified cow is returned, display the cow

    elif sys.argv[1]!="-l" and sys.argv[1]!="-n": #if both -l and -n are not present, display the default cow and message
        cow = find_cow("heifer", cows)  # default heifer cow is used
        message = ""
        if cow!=None:
            for i in sys.argv[1:]:
                message += i + " "
            print("\n",message,sep="")
            print(cow)
    pass

if __name__=="__main__": #code is ran if it's the main code.
    main()

# print(cows[0].get_name()) #FOR TESTING PURPOSES prints name of first cow object