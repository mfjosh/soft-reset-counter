#Version Number : 0.2.3
#####    ----       global flags
from tkinter import *
import os
import time
import msvcrt
from bindglobal import BindGlobal
import pyautogui
import threading

ws = Tk()
######     ----    Functions will be placed here
def file_validation():
    global file_path
    file_path ="counter.txt"
    #check if counter.txt exists
    if os.path.isfile(file_path):
        #open in read mode
        text_file = open(file_path,'r')
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()
        #print("File location: counter.txt")
    else:
        with open(file_path, 'w') as f:
            f.write("0")
            ftext_file = open(file_path, 'r')
            fdata = ftext_file.read()
            ftext_file.close()
            print("counter.txt created in directory")
def add_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = int(data1) + 1
    with open(file_path, 'w') as e:
        e.write(str(sum))
def subtract_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = int(data1) - 1
    with open(file_path, 'w') as e:
        e.write(str(sum))
def reset_counter():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = 0
    with open(file_path, 'w') as e:
        e.write(str(sum))
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
def addopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    add_number()
    openFile()
    txtarea.configure(state="disabled")
def subopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    subtract_number()
    openFile()
    txtarea.configure(state="disabled")
def resetopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    reset_counter()
    openFile()
    txtarea.configure(state="disabled")
def openFile():
    #open in read mode
    tf = open(file_path,'r')
    #read whole file to a string
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
def WindowSetttings():
    ws.title("Shiny Reset Counter")
    ws.geometry("475x650")
    ws['bg']='#F0F0F0'
def TextAreaConfig():
    global txtarea
    txtarea = Text(ws, width=5, height=0,bg='#F0F0F0', font=("Helvetica", 40))
    txtarea.place(x=100 ,y=100, height=95, width=150)
    txtarea.configure(state="disabled")
def Label1Config():
    var = StringVar()
    LabelTop = Label(ws,bg='#F0F0F0',fg="blue",textvariable=var,font=("Arial",12))
    var.set("File is generated and saved as counter.txt")
    LabelTop.place(x=25, y=0)
def Label2Config():
    var = StringVar()
    LabelTop = Label(ws,bg='#F0F0F0',fg="black",textvariable=var,font=("Arial",10))
    var.set("Odds 1/4096")
    LabelTop.place(x=0, y=400)
def Label3Config():
    var = StringVar()
    LabelTop = Label(ws,bg='#F0F0F0',fg="black",textvariable=var,font=("Arial",10))
    var.set("Created by : CorruptedJosh")
    LabelTop.place(x=0, y=425)
def HotKeyPress():
    bg = BindGlobal()
    bg.gbind('+',hotkeyadd)
    bg.gbind('-',hotkeysub)
    bg.gbind('*',hotkeyreset)
def MainButtons():
    Button(
        ws,
        text="add",
        height=2,
        width=10,
        command=lambda:addopen()
        ).place(x=100,y=200)
    Button(
        ws,
        text="subtract",
        height=2,
        width=10,
        command=lambda:subopen()
        ).place(x=180,y=200)
    Button(
        ws,
        text="reset",
        height=2,
        width=21,
        command=lambda:resetopen()
        ).place(x=100,y=241)
def hotkeyadd(event):
    addopen()
def hotkeysub(event):
    subopen()
def hotkeyreset(event):
    resetopen()

def printopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    #add_number()
    print_number()
    openFile()
    txtarea.configure(state="disabled")
####TESTING
def copyright_validation():
    ref_region = pyautogui.locateOnScreen('reference.png')
    time.sleep(1)
    if ref_region != None:
        addopen()
        while ref_region != None:
            ref_region = pyautogui.locateOnScreen('reference.png')
            time.sleep(1)
    ws.after(2000, start_copyright_validation_in_bg)
def start_copyright_validation_in_bg():
    threading.Thread(target=copyright_validation).start()

#### END TESTING

#### THIS IS FOR THE GUI
file_validation()
Label1Config()
TextAreaConfig()
WindowSetttings()
HotKeyPress()
MainButtons()
Label2Config()
Label3Config()
start_copyright_validation_in_bg()


ws.mainloop()
