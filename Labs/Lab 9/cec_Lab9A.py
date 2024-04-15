
def encode(password):
    encodedpassword=""
    for digit in password:
        char=int(digit)
        char+=3
        if char>9:
            char=char%3
        encodedpassword+=str(char)
    return encodedpassword
def main():
    print("Menu\n-------------\n)
if __name__=="__main__":
    main()