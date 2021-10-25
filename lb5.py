filename="mydata.txt"

def write(filename):
    fd = open(filename, "w")
    for i in range(11):
        A = i*10
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("запис файлу виконано")

import random

filename="mydata.txt"

def append(filename):
    fd=open(filename, "w")
    for i in range(11):
        A=random.uniform(1, 5)
        fd.write("%i\t%.1f\n"%(i, A))
    fd.close()
    print("дозапис у кінець файлу виконано")

import csv
import sys

filename="mydata.txt"

def read(filename):
    fd = open(filename, "r") 
    reader=csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()
    print("зчитування файлу виконано")

import shutil
import os

filename="mydata.txt"

def copy(filename):
    shutil.copyfile("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5\\mydata.txt", "C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5.txt")
    print("копіювання файлу виконано")

filename="mydata.txt"

def rename(filename):
    os.rename("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5\\mydata.txt", "C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5\\lab5.txt")
    print("перейменування файлу виконано") 

filename="mydata.txt"

def delete(filename):
    os.remove("C:\\Users\\Яна\\Desktop\\gavno-fit\\ICS-485270\\lab5\\mydata.txt")
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