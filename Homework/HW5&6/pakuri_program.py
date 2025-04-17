from pakudex import Pakudex #imports Pakudex class from pakudex.py
def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity=input("Enter max capacity of the Pakudex: ") #capacity variable is initialized based on user input
    while capacity.isdigit()==False or int(capacity)<1: #checks to see if the capacity is an actual number. Will continue looping until this is the case.
        print("Please enter a valid size.")
        capacity = input("Enter max capacity of the Pakudex: ")

    print("The Pakudex can hold",capacity,"species of Pakuri.")
    pakudex=Pakudex(capacity) #initializes pakudex object with specific capacity

    while True: #pakudex menu will keep being displayed as long as the while loop is true.
        print("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")
        option=input("\nWhat would you like to do? ") #option variable is initialized based on user input

        if option=="1": #list pakuri
            if len(pakudex.pakudexlist)==0: #list will not be displayed unless the pakudex list has at least one object
                print("No Pakuri in Pakudex yet!")
            else:
                count=1 #count variable initialized as 1. Increased by 1 for every species
                print("\nPakuri In Pakudex:")
                for species in pakudex.get_species_array(): #for loop goes through each species on the returned list from the get_species_array function and writes them out
                    print(f"{count}. {species}")
                    count+=1

        elif option=="2": #show pakuri stats
            name=input("Enter the name of the species to display: ")
            if pakudex.get_stats(name)==None: #if None is returned, print an error
                print("Error: No such Pakuri!")
            else: #If the list is returned, print the stats of that respective species at the indexes
                stats=pakudex.get_stats(name)
                print(f"\nSpecies: {name}\nAttack: {stats[0]}\nDefense: {stats[1]}\nSpeed: {stats[2]}")

        elif option=="3": #adding pakuri
            if int(pakudex.get_size())==int(pakudex.get_capacity()): #if the size of the pakudex equals the max capacity, print an error.
                print("Error: Pakudex is full!")
            else:
                name=input("Enter the name of the species to add: ")
                if pakudex.add_pakuri(name)==True: #if add_pakuri function returns true, the species was added successfully
                    print(f"Pakuri species {name} successfully added!")
                elif pakudex.add_pakuri(name)==False: #if the function returns false, the species is already in the pakudex
                    print("Error: Pakudex already contains this species!")

        elif option=="4": #evolving pakuri
            name=input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(name)==True: #if evolve_species function returns true, the species was evolved successfully
                print(f"{name} has evolved!")
            elif pakudex.evolve_species(name)==False: #if evolve_species function returns false, the species does not exist in the pakudex
                print("Error: No such Pakuri!")

        elif option=="5": #sort pakuri
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif option=="6": #exit
            print("Thanks for using Pakudex! Bye!")
            break

        else: #if a valid option isn't chosen, print an error message.
            print("Unrecognized menu selection!")

if __name__=="__main__": #checks to see if pakuri_program is the main program being ran.
    main()