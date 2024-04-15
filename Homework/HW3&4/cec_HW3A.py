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