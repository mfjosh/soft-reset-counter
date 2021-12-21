#global flags
import os
file_path ="counter.txt"

#Functions will be placed here
def file_validation():
    #check if counter.txt exists
    if os.path.isfile(file_path):
        #open in read mode
        text_file = open(file_path,'r')
        #read whole file to a string
        data = text_file.read()
        #close file
        text_file.close()
    else:
        with open(file_path, 'w') as f:
            f.write("0")
            ftext_file = open(file_path, 'r')
            fdata = ftext_file.read()
            ftext_file.close()
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
#Test to print number for validation
def print_number():
    #open in read mode
    text_file = open(file_path,'r')
    #read whole file to a string
    data = text_file.read()
    #close file
    text_file.close()
    print(data)


#Code begins here
file_validation()
add_number()
print_number()
