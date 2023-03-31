#Password Manager first iteration
#create and display passwords for users
#P.Patchigalla, April 2020

try:
    #initialise variables and lists
    name =""
    age = ""

    #Create an empty list to store usernames and passwords for web/apps
    password_list = []
    #Create a list with existing members and store new mmber deatials
    member_list = ["bdsc","pass123"]

    #Function prints out the menu for user to choose an option and return that value to main routine
    def menu(name, age):

        print("Hello",name)

        if age < 13:
            print("Sorry you do not qualify to open an account, ")
            exit() #the program terminates.

    #Function allows user to add username and password to password_list
    def add_details():
        while True:

            app = input("what is the name of web/app? or 'end' to the return menu: ").strip().lower()
            if app =="end":
                break
            else:
                username= input("What is the username of web/app? ")
                
                while True:
                    password = input("Enter password that is seven chracters long, includes capital letter and number: ").strip()
                    if (any(passreqs.isupper() for passreqs in password) and any(passreq.isdigit() for passreq in password) and len(password) >= 7):
                        password_list.append([app, username, password])
                        break
            
    #Function shows user naes and password stored in the list, for loop repeates printing usernames and passwords

    def view_list():
        print("Her is the list of passwords saved in Password Manager for you")
        for i in range(0, len(password_list)):
            print(i+1," Username: ",password_list[i][0], " Password: ",password_list[i][1], " Web/App name: ",password_list[i][2])
        

    name = input("What is your name? ")

    age = int(input("How old are you? "))
    menu(name, age)
    while True:
        member = input("Please enter L for log in or N fr creating new account: ")

        if member == "L":
            m_username = input("Enter username: ")
            m_password = input("Enter password: ")
            if m_username and m_password in member_list:
                print("Username and password match!!")
                break
        elif member == "N":
            m_username = input("Enter username: ")
            m_password = input("Enter password: ")
            member_list.append([m_username, m_password])
            print("Your account created!!")
            break
        else:
            print("That was not a valid option, please enter L for log in or N for creating a new account: ")
            
    while True:
        chosen_option = input("""choose a mode by entering the number: \n1: Add passwords \n2: View passwords \n3: Exit \n""").strip()

        if chosen_option == "1":
            #call add_tasks function if user chooses 1
            add_details()
        elif chosen_option == "2":
            #call view_tasks function if user presses 2
            view_list()
        elif chosen_option == "3":
            #say goodbye and end program
            break
        else:
            print("That was not a valid option, please try again")
        
    print("goodbye, thanks for using password manager")
except NameError:
    print("That is not an acceptable answer, try again")
except ValueError:
    print("That is not an acceptable answer")
    age = int(input("How old are you? "))

