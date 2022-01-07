###                                          Version Number : 0.2.7
#####    ----       global flags
from tkinter import * #used for GUI
from tkinter import font as font #used to have fancy font options
import os
import time
from bindglobal import BindGlobal #used for keybindings to set hotkeys
import pyautogui #used to capute screen for automation actions
import threading #used to prevent program from being lockedup compltely when automation is running

root = Tk()
#about is currently used for the about message under Help menubar
about = 'Automation is utilized by matching reference.png to the screen.'\
'With automation enabled, the program will count anytime the reference'\
'is visible. This can be utilized by screenshotting an unique visual,'\
'such as a copyright screen that appears during start-up to count your resets'\
'automatically. This feature seems to be quite laggy so use with caution'

#####    ----       Global Variables for button automation switch
stop_threads = False
# this should reduce lag in automation [pyautogui.PAUSE = 0]
pyautogui.PAUSE = 0
#is_on is for the automation switch
is_on = True
#####    ----       Functions will be placed here
#Get absolute path. I placed this here to see if I can make the executable file one file with images
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#END TEST

#file_validation checks whether or not counter.txt exists. If it does, it stores the value into file_path
#if not, it creates the file, writes 0, then stores the value into file_path
def file_validation():
    global file_path
    file_path ="counter.txt"
    #check if counter.txt exists
    if os.path.isfile(file_path):
        #open in read mode
        text_file = open(file_path,'r')
        #read whole file to a string
        data = text_file.read()
        text_file.close()
    else:
        with open(file_path, 'w') as f:
            f.write("0")
            ftext_file = open(file_path, 'r')
            fdata = ftext_file.read()
            ftext_file.close()
#Windowrootsettings is the basic information for the main window.
def Windorootsetttings():
    root.title("Shiny Reset Counter")
    root.geometry("375x500")
    root['bg']='#F0F0F0'
#add_number will validate the information in counter.txt is a number, if so it will add 1. Otherwise, it will append 0.
def add_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    if data1.isdigit():
        sum = int(data1) + 1
        with open(file_path, 'w') as e:
            e.write(str(sum))
    else:
        with open(file_path, 'w') as e:
            e.write('0')
    text1.close()
#subtract_number validates there is a valid positive within counter.txt, then subtracts 1 from it.
#If the file is empty (0 bites), contains alpha charactors, or a negative number it will append 0 to the file.
#If the number is positive, it will subtract 1.
def subtract_number():
    filesize = os.path.getsize(file_path)
    text1 = open(file_path,'r')
    data1 = text1.read()
    with open(file_path, 'w') as e:
        if data1.isalpha() or filesize == 0 or '-1' in data1:
            e.write('0')
        else:
            sum = int(data1) - 1
            e.write(str(sum))
    text1.close()
#reset_counter is used to set value to 0 in counter.txt
def reset_counter():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = 0
    with open(file_path, 'w') as e:
        e.write(str(sum))
    text1.close()
#print_number simply reads the number from counter.txt
def print_number():
    text_file = open(file_path,'r')
    data = text_file.read()
    text_file.close()
#addopen utilizes subtract_number() to decrease the value, then displays current value in GUI
def addopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    add_number()
    openFile()
    txtarea.configure(state="disabled")
#subopen utilizes subtract_number() to decrease the value, then displays current value in GUI
def subopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0, END)
    subtract_number()
    openFile()
    txtarea.configure(state="disabled")
#resetopen resets value to 0 by using reset_counter() then displays value in GUI
def resetopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0,END)
    reset_counter()
    openFile()
    txtarea.configure(state="disabled")
#openFile displays the current value in the GUI by reading counter.txt
def openFile():
    tf = open(file_path,'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
#TextAreaConfig is the window which displays the value. I have it disabled so the user cannot change value on accident.
#The commands which change the value, temporarily enable the field while adjusting the value
def TextAreaConfig():
    global txtarea
    txtarea = Text(root,width=5,height=0,bg='#F0F0F0',bd=0,font=("Poppins bold",40))
    txtarea.place(x=150 ,y=100, height=95, width=150)
    txtarea.configure(state="disabled")
#Below are labels that are configured on the main program.
def Label1Config():
    var = StringVar()
    LabelTop = Label(root,bg='#F0F0F0',fg="black",textvariable=var,font=("Poppins bold",12))
    var.set("File is generated and saved as counter.txt")
    LabelTop.place(x=25,y=0)
def Label2Config():
    var = StringVar()
    LabelTop = Label(root,bg='#F0F0F0',fg="black",textvariable=var,font=("Poppins bold",13))
    var.set("Odds 1/4096")
    LabelTop.place(x=0,y=450)
def Label3Config():
    var = StringVar()
    LabelTop = Label(root,bg='#F0F0F0',fg="black",textvariable=var,font=("Poppins bold",12))
    var.set("Created by: CorruptedJosh")
    LabelTop.place(x=0,y=470)
#HotKeyPress is used to track the keyboard buttons for the key bindings. At some point I would like to enable the user to set their own.
def HotKeyPress():
    bg = BindGlobal()
    bg.gbind('+',hotkeyadd)
    bg.gbind('-',hotkeysub)
    bg.gbind('*',hotkeyreset)
#MainButtons are the first sets of buttons that I have added. This is basically the configuration, placement, and commands.
def MainButtons():
    global buttonadd
    global buttonreset
    global buttonsubtract
    buttonadd = PhotoImage(file= resource_path("images\\add.png"))
    buttonsubtract = PhotoImage(file= resource_path("images\\subtract.png"))
    buttonreset = PhotoImage(file= resource_path("images\\reset.png"))



    add_ =Button(root,text="add",image=buttonadd,bd=0,height=45,width=78,font=font.Font(size=14),command=lambda:addopen()).place(x=70,y=200)
    subtract_ =Button(root,text="subtract",image=buttonsubtract,bd=0,height=45,width=114,font=font.Font(size=14),command=lambda:subopen()).place(x=150,y=200)
    reset_ =Button(root,text="reset",image=buttonreset,bd=0,height=45,width=88,font=font.Font(size=14),command=lambda:resetopen()).place(x=115,y=245)
#The hotkey buttons below are the events triggered when the hotkeys are pressed
def hotkeyadd(event):
    addopen()
def hotkeysub(event):
    subopen()
def hotkeyreset(event):
    resetopen()
#printopen shows the value within the GUI by using print_number()
def printopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0,END)
    print_number()
    openFile()
    txtarea.configure(state="disabled")
#validationinbgrun is the reference validation used when automation is toggled to enabled
def validationinbgrun():
    global stop_threads
    while True:
        ref_region=pyautogui.locateOnScreen('reference.png')
        if ref_region!=None:
            addopen()
            while ref_region!=None:
                ref_region=pyautogui.locateOnScreen('reference.png')
            root.after(1,validationinbgrun())
        if stop_threads:
            break
#startcvibg is to create threads so the automation does not lock the entire program
def startcvibg():
        threading.Thread(target=validationinbgrun).start()
#button_mode is for the automation button.
def button_mode():
   global is_on
   global on
   global off
   global stop_threads
   on = PhotoImage(file= resource_path("images\on.png"))
   off = PhotoImage(file= resource_path("images\off.png"))
   on_= Button(root,image=on,bd=0,command=button_mode)
   on_.place(x=120,y=330)
   label = Label(root,text = "Automation is Off / Toggle to enable",fg ="black",font =("Poppins bold",12))
   label.place(x=100,y=300)
   #Determine it is on or off
   if is_on:
      on_.config(image=off)
      label.config(text="Automation is Off", fg="black")
      is_on=False
      stop_threads=True
      print('function stopped')
   else:
      on_.config(image=on)
      label.config(text ="Automation is On", fg="black")
      is_on=True
      stop_threads=False
      startcvibg()
      print('function running')
#AboutHelp function is to create new window for the about secion under Help menubar.
def AboutHelp():
   filewin = Toplevel(root)
   var = StringVar()
   LabelTop = Label(filewin, bg='#F0F0F0',fg="black",textvariable=var,font=("Poppins bold",10), wraplength=375)
   var.set(about)
   LabelTop.pack()
   button = Button(filewin, bg='#F0F0F0', fg="black",text="close", command=filewin.destroy)
   button.pack()


#####    ----       THIS IS THE GUI

#Start of topLevel Menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_separator()
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=AboutHelp)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
#End of topLevel Menubar

file_validation()
Label1Config()
TextAreaConfig()
Windorootsetttings()
HotKeyPress()
MainButtons()
Label2Config()
Label3Config()
printopen()
button_mode()

#####    ----       End of Program
root.mainloop()
