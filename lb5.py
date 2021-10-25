filename="mydata.txt"

def write(filename):
    # Відкриття файлу
    fd = open(filename, "w") 
    # Запис у файл
    for i in range(10):     
        A = i*18     
        fd.write("%i\t%.1f\n" % (i, A)) 
    # Закриття файлу
    fd.close() 

import random

filename="mydata.txt"

def append(filename):
    #Відкриття файлу
    fd=open(filename, "w")
    #Запис у файл
    for i in range(10):
        A=random.uniform(2, 5)
        fd.write("%\t%.lf\n"%(i,A))
    #Закриття файлу
    fd.close()
    print("дозапис у кінець файлу виконано")

import csv
import sys

filename="mydata.txt"

def read(filename):
    # Відкриття файлу
    fd = open(filename, "w") 
    #Читання даних
    reader=csv.reader(fd, delimiter="\t")
    #Виведення зиісту файлу
    for row in reader:
        print(row)
    #Закриття файлу
    fd.close()
    print("зчитування файлу виконано")

import shutil
import os

def copy(filename):
    shutil.copyfile("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5", "C:\\Users\\Яна\\Documents\\Documents")
    print("копіювання файлу виконано")

def rename(filename):
    os.rename("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\mydata.txt", "lab5.txt")
    print("перейменування файлу виконано") 

def delete(filename):
    os.remove("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\mydata.txt")
    print("видалення файлу виконано")

filename = "mydata.txt"
x=int(input("виберіть режим роботи з файлом: \n :: 1 - читати з файла :: \n :: 2 - записати у файл :: \n :: 3 - дозапис у файл :: \n :: 4 - перейменувати файл :: \n :: 5 - видалити файл :: \n :: 6 - зробити копію файлу ::\n"))          

mode=' '
if x==1:
    read(filename)
elif x==2:
    write(filename)
elif x==3:
    append(filename) 
elif x==4:
    rename(filename)
elif x==5:
    delete(filename)         
elif x==6:
    copy(filename)
else:
    print("такого варіанту не існує")    
input('Press ENTER to exit')

