#Version Number : 0.2.5
#####    ----       global flags
from tkinter import *
from tkinter import font as font
import os
import time
import msvcrt
from bindglobal import BindGlobal
import pyautogui
import threading

root = Tk()
#####    ----       Global Variables for button automation switch
stop_threads = False
# this should reduce lag in automation [pyautogui.PAUSE = 0]
pyautogui.PAUSE = 0
#is_on is for the automation switch
is_on = True
#####    ----       Functions will be placed here
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
def Windorootetttings():
    root.title("Shiny Reset Counter")
    root.geometry("375x500")
    root['bg']='#F0F0F0'
def add_number():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()

    if data1.isdigit():
        sum = int(data1) + 1
        with open(file_path, 'w') as e:
            e.write(str(sum))
    else:
        with open(file_path, 'w') as e:
            e.write('0')
def subtract_number():
    filesize = os.path.getsize(file_path)
    text1 = open(file_path,'r')
    data1 = text1.read()
    with open(file_path, 'w') as e:
        if data1.isalpha() or filesize == 0:
            e.write('0')
        elif '-1' in data1:
            e.write('0')
        else:
            sum = int(data1) - 1
            e.write(str(sum))
    #text1.close()
def reset_counter():
    text1 = open(file_path,'r')
    data1 = text1.read()
    text1.close()
    sum = 0
    with open(file_path, 'w') as e:
        e.write(str(sum))
def print_number():
    text_file = open(file_path,'r')
    data = text_file.read()
    text_file.close()
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
    txtarea.delete(1.0,END)
    reset_counter()
    openFile()
    txtarea.configure(state="disabled")
def openFile():
    tf = open(file_path,'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
def TextAreaConfig():
    global txtarea
    txtarea = Text(root,width=5,height=0,bg='#F0F0F0',bd=0,font=("Poppins bold",40))
    txtarea.place(x=150 ,y=100, height=95, width=150)
    txtarea.configure(state="disabled")
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
def HotKeyPress():
    bg = BindGlobal()
    bg.gbind('+',hotkeyadd)
    bg.gbind('-',hotkeysub)
    bg.gbind('*',hotkeyreset)
def MainButtons():
    buttonadd = PhotoImage(file="add.png")
    buttonsubtract = PhotoImage(file="subtract.png")
    buttonreset = PhotoImage(file="reset.png")

    add_ =Button(root,text="add",bd=0,height=2,width=10,font=font.Font(size=14),command=lambda:addopen()).place(x=70,y=200)
    subtract_ =Button(root,text="subtract",bd=0,height=2,width=10,font=font.Font(size=14),command=lambda:subopen()).place(x=150,y=200)
    reset_ =Button(root,text="reset",bd=0,height=2,width=21,font=font.Font(size=14),command=lambda:resetopen()).place(x=50,y=241)
def hotkeyadd(event):
    addopen()
def hotkeysub(event):
    subopen()
def hotkeyreset(event):
    resetopen()
def printopen():
    txtarea.configure(state="normal")
    txtarea.delete(1.0,END)
    print_number()
    openFile()
    txtarea.configure(state="disabled")
def copyright_validation():
    pyautogui.PAUSE=0
    ref_region=pyautogui.locateOnScreen('reference.png')
    if ref_region!=None:
        addopen()
        while ref_region!=None:
            ref_region=pyautogui.locateOnScreen('reference.png')
        root.after(1,copyright_validation())
        print('test1')
def start_copyright_validation_in_bg():
    threading.Thread(target=copyright_validation).start()
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
def startcvibg():
        threading.Thread(target=validationinbgrun).start()
def button_mode():
   global is_on
   global on
   global off
   global stop_threads
   on = PhotoImage(file="on.png")
   off = PhotoImage(file="off.png")
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

#####    ----       THIS IS THE GUI
file_validation()
Label1Config()
TextAreaConfig()
Windorootetttings()
HotKeyPress()
MainButtons()
Label2Config()
Label3Config()
button_mode()

#####    ----       End of Program
root.mainloop()
