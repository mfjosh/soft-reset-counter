#Version Number : 0.1.2
#####    ----       global flags
import os
file_path ="counter.txt"
import keyboard
import time
import msvcrt


######     ----    Functions will be placed here
def file_validation():
    #check if counter.txt exists
    if os.path.isfile(file_path):
        #open in read mode
        text_file = open(file_path,'r')
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()
        print("File location: counter.txt")
    else:
        with open(file_path, 'w') as f:
            f.write("0")
            ftext_file = open(file_path, 'r')
            fdata = ftext_file.read()
            ftext_file.close()
            print("counter.txt created in directory")
 #add numbers to the existing text
def add_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = int(data1) + 1
    with open(file_path, 'w') as e:
        e.write(str(sum))
 #subtract 1 from the number
def subtract_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = int(data1) - 1
    with open(file_path, 'w') as e:
        e.write(str(sum))
 #reset counter to Zero
def reset_counter():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = 0
    with open(file_path, 'w') as e:
        e.write(str(sum))
 #Test to print number for validation
def print_number():
    #open in read mode
    text_file = open(file_path,'r')
    #read whole file to a string
    data = text_file.read()
    #close file
    text_file.close()
    print(data)
def get_menu_choice():
    def print_menu():       # Your menu design here
        print(30 * "-", "SHINY COUNTER MENU", 30 * "-")
        print("The Current Count is: ", end=""), print_number()
        print("")
        print("")
        print("")
        print("1. Add ")
        print("2. Subtract ")
        print("3. Reset Counter ")
        print("4. Exit ")
        #print("5. Example Text ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        #choice = input("Enter your choice [1-5]: ")
        choice = msvcrt.getch().decode('ASCII')

        if choice == '1':
            add_number()
        elif choice == '2':
            subtract_number()
        elif choice == '3':
            reset_counter()
        elif choice == '4':
            print("Exiting..")
            exit()
        elif choice == '5':
            int_choice = -1
            #Example Command here
            loop = False  # This will make the while loop to end
        elif choice == '+':
            add_number()
        elif choice == '-':
            subtract_number()
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]
    print(get_menu_choice())

#Code begins here
file_validation()
get_menu_choice()
