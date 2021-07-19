s=[]
from os import system

def menu():
    ch=0
    while(ch<1 or ch>4):
        print("\n"*30)
        print("\n\n\n\n\n")
        print("\t\t\t1: Push")
        print("\t\t\t2: Pop")
        print("\t\t\t3: Display")
        print("\t\t\t4: EXIT")
        ch=int(input("\n\t\t\tEnter your choice(1-4) : "))
    return ch

def push():
    item=int(input("\t\t\tEnter an item to push:"))
    s.append(item)
    print("\t\t\tItem ",item," Pushed in the Stack")

def pop():
    if(s==[]):
        print("\t\t\tNO Item to pop")
    else:
        item=s.pop()
        print("\t\t\tItem ",item," Poped from Stack")
    
def display():
    if(s==[]):
        print("\t\t\tEmpty Stack")
    else:
        print("\t\t\t")
        for i in s:
            print(i," ",end="")

import sys
ch=0

while(ch!=4):
    ch=menu()
    if(ch==1):
        push()
    elif(ch==2):
        pop()
    elif(ch==3):
        display()
    elif(ch==4):
        print("\t\t\tAborting Program...........")
        sys.exit()
    av=input("\n\t\t\tPress any key to continue.....\n")
