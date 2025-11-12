from pathlib import Path
import os
#crud

def createfolder():
    name = input(" enter your folder name: ")
    p = Path(name) # it will create the path of the folder
    p.mkdir()# it will create folder
# createfolder()

def readfolder(): 
    p = Path("")
    item = list (p.rglob("*")) # it give all the files in current file
    for i , v in enumerate(item):
        print(i+1,v) # i = index , v = element 
readfolder()


def deletefolder():
    readfolder()
    name = input("enter folder name to be deleted : ")
    p = Path(name)
    if p.exists():
        p.rmdir()
        print("folder deleted")
    else:
        print("no folder exists")


def updatefolder():
    oldname = input(" enter folder name: ")
    p = Path(oldname)
    if p.exists():
        new_name = input("enter your new name: ")
        new_p = Path(new_name)
        p.rename(new_p)
        print("folder renamed")
    
def createfile():
    name = input(" enter your file name")
    p = Path(name)
    if not p.exists():
        with open(name,'w') as fs:
            data = input("enter your data ")
            fs.write(data)
            print("file will write succesfully")


def  readfile():
    readfolder()
    name = input(" enter your file name (with extension): ")
    p = Path(name)
    if p.exists and p.is_file():
        with open (name,'r') as fs:
            print(fs.read())

def deletefile():
    
    name = input(" enter your file name (with extension): ")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("file deleted succesfully")

def updatefile():
    name = input("enter the filr name with extension")
    p = Path(name)
    if p.exists() and p.is_file() :
        print("Press 1 for renaming the file")
        print("Press 2 for appending the file")
        print("Press 3 for overwriting the file")
        choice = int(input("enter your choice"))
        if choice ==1:
            new_name = input("enter new name for file")
            new_p = Path(new_name)
            p.rename(new_p)
            print("file name change successfully")
        if choice == 2:
            readfile()
            with open(name,'a') as fs:
                data = input("enter your data ")
                fs.write(data)
        if choice == 3 :
            with open(name,'w') as fs:
                data = input("enter your data")
                fs.write(data)
                
    
        
while True:
    print("Press 1 for creating folder ")
    print("Press 2 for reading folder")
    print(" press 3 for deleting folder")
    print("Press 0 for exiting.. ")
    print("press 4 for update the folder")
    print("press 5 to create the file")
    print("press 6 to read the file")
    print("press 7 for delete file")
    print("press 8 for update the file")
    
    choice = int(input("enter your choice: "))
    if choice == 1:
        createfolder()
    if choice == 2:
        readfolder()
    if choice == 3:
        deletefolder()
    if choice == 4:
        updatefolder()
    if choice == 5:
       createfile() 
    if choice == 6 :
        readfile()
    if choice ==7:
        deletefile()
    if choice == 8:
        updatefile()
    if choice == 0:
       break
