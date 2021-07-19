l=[]
from os import system

def menu():
    ch=0
    while(ch<1 or ch>4):
        print("\n"*30)
        print("\n\n\n\n\n")
        print("\t\t\t1: Insert")
        print("\t\t\t2: Delete")
        print("\t\t\t3: Display")
        print("\t\t\t4: EXIT")
        ch=int(input("\n\t\t\tEnter your choice(1-4) : "))
    return ch

def insert():
    pos=int(input("\t\t\tEnter the Position:"))
    pos=pos-1
    if(pos>=0 and pos<=len(l)):
            item=int(input("\t\t\tEnter an item to insert"))
            l.insert(pos,item)
            print("\t\t\tItem ",item," inserted in the list")
    else:
            print("\t\t\tInvalid Position")                    

def Delete():
    if(l==[]):
        print("\t\t\tNO Item to Delete")
    else:
        pos=int(input("\t\t\tEnter the position"))
        pos=pos-1
        if(pos>=0 and pos< len(l)):
                item=l.pop(pos)
                print("\t\t\tItem ",item," Deleted from List")
        else:
                print("\t\t\tInvalid position")
                
def display():
    if(l==[]):
        print("\t\t\tEmpty List")
    else:
        print("\n\t\t\t",end="")
        for i in l:
            print(i," ",end="")

import sys
ch=0

while(ch!=4):
    ch=menu()
    if(ch==1):
        insert()
    elif(ch==2):
        Delete()
    elif(ch==3):
        display()
    elif(ch==4):
        print("\t\t\tAborting Program...........")
        sys.exit()
    av=input("\n\t\t\tPress any key to continue.....\n")
