q=[]
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
    item=int(input("\t\t\tEnter an item to Insert:"))
    q.append(item)
    print("\t\t\tItem ",item," Insert in the Queue")

def Delete():
    if(q==[]):
        print("\t\t\tNO Item to Delete")
    else:
        item=q.pop(0)
        print("\t\t\tItem ",item," Deleted from Queue")
    
def display():
    if(q==[]):
        print("\t\t\tEmpty Queue")
    else:
        print("\n\t\t\t",end="")
        for i in q:
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
