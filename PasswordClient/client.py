from Password import Password
import pickle

def main():

    ADMIN_PASS = "12345"
    
    f = open("data.pkl", "rb")
    passwords = pickle.load(f)
    f.close()
    
    choice = "0"
    print("Welcome to the Password Manager.")
    attempt = input("Please enter the admin password to enter: ")
    
    while(attempt != ADMIN_PASS):
        print("\nIncorrect. Please try again")
        attempt = input("Please enter the admin password to enter: ")
        
    print("Correct! Welcome.\n")
    while(choice != "3"):
        
        print("Menu")
        print("----------")
        print("1. Enter a new password")
        print("2. View Passwords")
        print("3. Quit")

        choice = input("What would you like to do? ")

        if(choice.isalpha()):
                print("Please enter a numeric value.\n")
        elif(int(choice) not in range(1,4)):
                print("Enter a valid option.\n")


        if(choice == "1"):

            website = input("What is the website? ")
            author = input("What is the email? ")
            text = input("What is the password? ")

            pass_obj = Password(author, text, website)
            passwords.append(pass_obj)
            print("Your information has been saved!\n")

        elif(choice == "2"):
            
            print("Passwords")
            print("-------------\n")

            if(len(passwords) == 0):
                print("No Passwords available");
            else:
                for i in range(len(passwords)):
                    print(passwords[i].get_site())
                    print(passwords[i].get_author())
                    print(passwords[i].get_text(), "\n")
                    print("-------------\n")
                    

        elif(choice == "3"):

            f = open("data.pkl", "wb")
            pickle.dump(passwords, f)
            f.close()
            print("Thank for using the Password Manager!")
   



main()
    
